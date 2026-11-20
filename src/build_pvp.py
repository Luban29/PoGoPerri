# Zapíše docs/data/pvp.json: top 100 Pokémonů pro Great, Ultra a Master League z PvPoke
# a ke každému detail (staty v lize, všechny útoky s PvP hodnotami, výhry a prohry).
# Vstupy: gm/pvpoke.json, gm/alex.json (CP multiplikátory, tabulka typů), gm/rank/r1500|r2500|r10000.json
import json, math

TOP = 100
PV = json.load(open('gm/pvpoke.json'))
GM = json.load(open('gm/alex.json'))
LEAGUES = [('great', 1500, 'gm/rank/r1500.json'), ('ultra', 2500, 'gm/rank/r2500.json'), ('master', 10000, 'gm/rank/r10000.json'),
           ('megagreat', 1500, 'gm/rank/m1500.json'), ('megaultra', 2500, 'gm/rank/m2500.json'), ('megamaster', 10000, 'gm/rank/m10000.json')]
TYPES = ['normal','fighting','flying','poison','ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic','ice','dragon','dark','fairy']

cpm_int = None; teff = {}
for e in GM:
    d = e['data']
    if 'playerLevel' in d and cpm_int is None: cpm_int = d['playerLevel']['cpMultiplier']
    if 'typeEffective' in d:
        t = d['typeEffective']; teff[t['attackType'].replace('POKEMON_TYPE_', '').lower()] = t['attackScalar']

def cpm(level):
    lo = int(math.floor(level))
    if level == lo: return cpm_int[lo - 1]
    a, b = cpm_int[lo - 1], cpm_int[lo]
    return math.sqrt((a * a + b * b) / 2)

def cp(bs, iv, level):
    m = cpm(level)
    return max(10, math.floor((bs['atk'] + iv[0]) * math.sqrt(bs['def'] + iv[1]) * math.sqrt(bs['hp'] + iv[2]) * m * m / 10))

def defense_chart(types):
    out = {}
    for at in TYPES:
        m = 1.0
        for t in types:
            m *= teff[at][TYPES.index(t)]
        if abs(m - 1) > 1e-6: out[at] = round(m, 3)
    return out

POKE = {p['speciesId']: p for p in PV['pokemon']}
MOVES = {m['moveId']: m for m in PV['moves']}

def move_info(mid):
    m = MOVES[mid]
    o = {'n': m['name'], 't': m['type'], 'p': m['power']}
    if m.get('energyGain'):
        o.update(e=m['energyGain'], tu=m.get('turns', max(1, m['cooldown'] // 500)))
    else:
        o.update(c=m['energy'])
    if m.get('buffs'):
        o.update(b=m['buffs'], bt=m.get('buffTarget'), bc=float(m.get('buffApplyChance', 1)))
    return o

used_moves = set()
out = {'leagues': {}, 'moves': {}, 'names': {}}
for key, cap, path in LEAGUES:
    rank = json.load(open(path))
    rows = []
    mega_only = key.startswith('mega')
    pool = [(i, r) for i, r in enumerate(rank) if (not mega_only) or 'mega' in POKE.get(r['speciesId'], {}).get('tags', [])]
    for oi, r in (pool if mega_only else pool[:TOP]):
        sid = r['speciesId']; p = POKE[sid]
        types = [t for t in p['types'] if t != 'none']
        tags = p.get('tags', [])
        kind = 'shadow' if 'shadow' in tags else (('primal' if 'primal' in sid else 'mega') if 'mega' in tags else '')
        if cap == 10000:
            iv = [15, 15, 15]; lvl = 50
        else:
            dv = p.get('defaultIVs', {}).get('cp%d' % cap)
            lvl, iv = (dv[0], dv[1:4]) if dv else (50, [15, 15, 15])
        elite = set(p.get('eliteMoves', []) + p.get('legacyMoves', []))
        tot_f = sum((m.get('uses') or 0) for m in r['moves']['fastMoves']) or 1
        tot_c = sum((m.get('uses') or 0) for m in r['moves']['chargedMoves']) or 1
        use_f = {m['moveId']: round(100 * (m.get('uses') or 0) / tot_f) for m in r['moves']['fastMoves']}
        use_c = {m['moveId']: round(100 * (m.get('uses') or 0) / tot_c) for m in r['moves']['chargedMoves']}
        fast = [m for m in p['fastMoves'] if m in MOVES]
        charged = [m for m in p['chargedMoves'] if m in MOVES]
        for m in [r['moveset'][0]] + list(use_f):
            if m in MOVES and m not in fast: fast.append(m)
        for m in r['moveset'][1:] + list(use_c):
            if m in MOVES and m not in charged: charged.append(m)
        for m in fast + charged + r['moveset']: used_moves.add(m)
        for o in r.get('matchups', []) + r.get('counters', []):
            out['names'][o['opponent']] = POKE.get(o['opponent'], {}).get('speciesName', o['opponent'])
        rows.append({
            'id': sid, 'n': p['speciesName'], 'dex': p['dex'], 'ty': types, 'k': kind,
            's': r['score'], 'sc': r['scores'], 'ms': r['moveset'],
            'lv': lvl, 'iv': iv, 'cp': cp(p['baseStats'], iv, lvl), 'bs': p['baseStats'],
            'st': r.get('stats', {}),
            'f': [[m, use_f.get(m, 0), 1 if m in elite else 0] for m in fast],
            'c': [[m, use_c.get(m, 0), 1 if m in elite else 0] for m in charged],
            'w': [[o['opponent'], o['rating']] for o in r.get('matchups', [])],
            'l': [[o['opponent'], o['rating']] for o in r.get('counters', [])],
            'def': defense_chart(types), 'or': oi + 1,
        })
    out['leagues'][key] = rows
for m in used_moves:
    out['moves'][m] = move_info(m)
out['updated'] = PV.get('timestamp')
json.dump(out, open('../docs/data/pvp.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print({k: len(v) for k, v in out['leagues'].items()}, len(out['moves']), 'moves')
