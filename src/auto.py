# Automatická aktualizace z ScrapedDuck (data z Leek Duck), spouští se po bosses.py a events.py.
# - Raidy: přidá bosse, kteří jsou podle Leek Duck v raidech teď a v seznamu chybí, a ukončí ty, kteří už v raidech nejsou.
# - Max Battles: přidá Max Monday bosse, kteří chybí.
# - Události: přidá eventy, které v events.py ještě nejsou (jen název, čas, kategorie a odkaz; české detaily doplní týdenní kontrola).
# Ruční data z bosses.py a events.py mají vždy přednost.
import json, re, unicodedata
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

TZ = ZoneInfo('Europe/Prague')
NOW = datetime.now(TZ).replace(tzinfo=None)
FMT = '%Y-%m-%dT%H:%M'
def fold(t): return re.sub(r'[^a-z0-9]+', ' ', unicodedata.normalize('NFD', t.lower()).encode('ascii', 'ignore').decode()).strip()
def local(s):
    if not s: return None
    if s.endswith('Z'): return datetime.fromisoformat(s[:-1]).replace(tzinfo=ZoneInfo('UTC')).astimezone(TZ).replace(tzinfo=None)
    return datetime.fromisoformat(s[:19])
def load(p):
    try: return json.load(open(p))
    except Exception as e: print('skip', p, e); return None

pve = json.load(open('../docs/data/pve.json'))
BYNAME = {fold(m[1]): m for m in pve['mons']}
IDS = {m[0]: m for m in pve['mons']}
REG = {'Alolan': 'Alolan', 'Galarian': 'Galarian', 'Hisuian': 'Hisuian', 'Paldean': 'Paldean'}
def find(name):
    n = re.sub(r'\s+', ' ', name.replace('’', "'")).strip()
    cands = [n]
    m = re.match(r'(Mega|Primal) (.+?)( [XY])?$', n)
    if m: cands.append('%s (%s%s)' % (m.group(2), m.group(1), m.group(3) or ''))
    m = re.match(r'(Alolan|Galarian|Hisuian|Paldean) (.+)$', n)
    if m: cands.append('%s (%s)' % (m.group(2), m.group(1)))
    m = re.match(r'(.+) \((.+?)( Forme| Form| Style)?\)$', n)
    if m: cands += ['%s (%s)' % (m.group(1), m.group(2)), m.group(1)]
    base = re.sub(r' wearing .*$', '', n)
    cands += [base, base.split(' ')[-1]]  # kostýmy: "Espeon wearing a sun scarf", "Sun Crown Pikachu"
    for c in cands:
        if fold(c) in BYNAME: return BYNAME[fold(c)][0]
    return None

# ---------- Raidy a Max Battles ----------
BS = json.load(open('../docs/data/bosses.json'))
TIER = {'1-Star Raids': '1', '3-Star Raids': '3', '5-Star Raids': '5', 'Mega Raids': 'mega', 'Primal Raids': 'mega', 'Mega Legendary Raids': 'mega'}
sd = load('gm/sd_raids.json')
log = []
if sd:
    live = set()
    for r in sd:
        t = TIER.get(r['tier']); name = r['name']
        if not t: continue
        shadow = name.startswith('Shadow ')
        if shadow: name = name[7:]; t = 's' + t
        sid = find(name)
        if not sid: log.append('neznámý raid boss: ' + r['name']); continue
        live.add((t, sid))
        cur = [b for b in BS['raids'] if b['t'] == t and b['id'] == sid and local(b['a']) <= NOW < local(b['b'])]
        if not cur:
            BS['raids'].append({'t': t, 'id': sid, 'n': ('Shadow ' if shadow else '') + IDS[sid][1], 'a': NOW.strftime(FMT),
                                'b': (NOW + timedelta(days=7)).strftime('%Y-%m-%dT22:00'), 'auto': 1})
            log.append('nový raid boss: ' + r['name'])
    if live:  # bossové, kteří podle Leek Duck v raidech už nejsou
        for b in BS['raids']:
            if local(b['a']) <= NOW < local(b['b']) and (b['t'], b['id']) not in live and local(b['a']) < NOW - timedelta(hours=12):
                b['b'] = NOW.strftime(FMT); log.append('konec raidu: ' + b['n'])
BS['raids'] = [b for b in BS['raids'] if local(b['b']) > NOW - timedelta(days=1)]

ev = load('gm/sd_events.json') or []
TIERS = {m[0]: m[2] for m in BS['maxbosses'] if m[2] != 'gmax'}
for e in ev:
    if e['eventType'] != 'max-mondays': continue
    m = re.match(r'Dynamax (.+?) during', e['name'])
    a = local(e['start'])
    if not m or not a: continue
    sid = find(m.group(1))
    if not sid: log.append('neznámý Max boss: ' + e['name']); continue
    if any(x['id'] == sid and abs((local(x['a']) - a).days) < 3 for x in BS['max']): continue
    t = TIERS.get(sid, '1')
    BS['max'].append({'t': t + '★ · Max Monday', 'id': sid, 'n': 'Dynamax ' + IDS[sid][1], 'a': a.strftime(FMT),
                      'b': (a + timedelta(days=6)).strftime('%Y-%m-%dT21:00'),
                      'note': 'Týdenní Max Battles %d. %d. – %d. %d.' % (a.day, a.month, (a + timedelta(days=6)).day, (a + timedelta(days=6)).month), 'auto': 1})
    log.append('nový Max boss: ' + e['name'])
BS['max'] = [b for b in BS['max'] if local(b['b']) > NOW - timedelta(days=1)]
BS['max'].sort(key=lambda b: b['a'])
json.dump(BS, open('../docs/data/bosses.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# ---------- Události ----------
EV = json.load(open('../docs/data/events.json'))
CAT = {'community-day': 'cd', 'go-battle-league': 'gbl', 'max-battles': 'max', 'max-mondays': 'max', 'pokemon-spotlight-hour': 'spotlight',
       'raid-battles': 'raid', 'raid-day': 'raid', 'raid-hour': 'raid'}
SKIP = {'season', 'go-pass', 'twitch-drops', 'max-mondays'}  # Max Monday bossy ukazuje záložka Max Battles
SUM = {'cd': 'Community Day: zvýšený výskyt featured Pokémona, exkluzivní útok a bonusy.', 'raid': 'Raidy s novým bossem.',
       'max': 'Max Battles s novým bossem.', 'spotlight': 'Spotlight Hour: hodina zvýšeného výskytu jednoho Pokémona a bonus.',
       'gbl': 'Nové ligy v GO Battle League.', 'event': 'Event v Pokémon GO.'}
def slug(u): return (re.search(r'leekduck\.com/events/([^/]+)', u or '') or [None, None])[1]
have_slugs = {slug(x.get('src')) for x in EV['events']} | {x['id'] for x in EV['events']}
have = [(local(x['start']), x['cat'], fold(x['title']), local(x['end'])) for x in EV['events']]
added = 0
for e in ev:
    if e['eventType'] in SKIP or e['eventID'] in have_slugs: continue
    a, b = local(e['start']), local(e['end'])
    if not a or not b or b < NOW: continue
    cat = CAT.get(e['eventType'], 'event')
    if any(t == fold(e['name']) or (s and s.date() == a.date() and (c == cat or (en and en.date() == b.date()))) for s, c, t, en in have): continue
    EV['events'].append({'id': e['eventID'], 'cat': cat, 'title': e['name'], 'start': a.strftime(FMT), 'end': b.strftime(FMT), 'auto': 1,
        'summary': SUM[cat], 'sections': [{'h': 'Podrobnosti', 'list': ['Podrobnosti zatím doplňujeme, celý popis najdeš na Leek Duck (odkaz níž).']}],
        'src': e['link']})
    added += 1; log.append('nový event: ' + e['name'])
if added: EV['updated'] = NOW.strftime('%Y-%m-%d')
json.dump(EV, open('../docs/data/events.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('\n'.join(log) or 'beze změn')

# ---------- Questy (Field Research) -> docs/data/quests.json ----------
# Úkoly bez typu jsou eventové, ostatní sezónní. Eventový úkol se přiřadí k eventu z events.json, v jehož textu je některá
# z odměn; když sedí jen na skončené eventy, je to zbytek po eventu a vynechá se. CP = 100 % IV na levelu 15 (odměna z úkolu).
rs = load('gm/sd_research.json')
if rs:
    CATQ = [('catch', 'Chytání'), ('throw', 'Házení'), ('battle', 'Souboje a raidy'), ('explore', 'Průzkum a vajíčka'),
            ('training', 'Trénink a evoluce'), ('buddy', 'Buddy a přátelé'), ('rocket', 'Team GO Rocket'), ('sponsored', 'Sponzorované'), ('ar', 'AR')]
    def task(x):
        return {'t': re.sub(r'<[^>]+>', '', x['text']).strip(),
                'r': [[w['name'], (w.get('combatPower') or {}).get('max'), 0, find(w['name'].split(' wearing')[0]) or ''] for w in x['rewards']]}
    evtext = [(e, fold(json.dumps(e, ensure_ascii=False))) for e in EV['events'] if e['cat'] not in ('partner',)]
    groups, other = {}, []
    for x in rs:
        if x.get('type'): continue
        names = [fold(w['name'].split(' wearing')[0]) for w in x['rewards']]
        score = {e['id']: sum(1 for n in names if n and re.search(r'\b' + re.escape(n) + r'\b', txt)) for e, txt in evtext}
        hits = [e for e, txt in evtext if 2 * score[e['id']] >= len(names)]
        live = [e for e in hits if local(e['end']) > NOW]
        if hits and not live: continue
        if live:  # nejvíc shodných odměn, při shodě nejnovější event
            e = sorted(live, key=lambda e: (score[e['id']], local(e['start'])))[-1]
            groups.setdefault(e['id'], {'ev': e['title'], 'id': e['id'], 'end': e['end'], 'tasks': []})['tasks'].append(task(x))
        else: other.append(task(x))
    ev_out = list(groups.values())
    if other: ev_out.append({'ev': 'Další eventové úkoly', 'id': '', 'end': '', 'tasks': other})
    season = [{'cat': name, 'tasks': [task(x) for x in rs if x.get('type') == k]} for k, name in CATQ]
    season = [c for c in season if c['tasks']]
    known = {k for k, _ in CATQ}
    extra = [task(x) for x in rs if x.get('type') and x['type'] not in known]
    if extra: season.append({'cat': 'Ostatní', 'tasks': extra})
    json.dump({'updated': NOW.strftime('%Y-%m-%d'), 'event': ev_out, 'season': season},
              open('../docs/data/quests.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print('questy:', sum(len(g['tasks']) for g in ev_out), 'eventových,', sum(len(c['tasks']) for c in season), 'sezónních')
