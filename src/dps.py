import json, math, sys
GM=json.load(open('gm/alex.json'))
PV=json.load(open('gm/pvpoke.json'))
ms={}; teff={}
for e in GM:
    d=e['data']
    if 'moveSettings' in d: ms[d['moveSettings']['movementId']]=d['moveSettings']
    if 'typeEffective' in d:
        t=d['typeEffective']; teff[t['attackType'].replace('POKEMON_TYPE_','').lower()]=t['attackScalar']
TYPES=['normal','fighting','flying','poison','ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic','ice','dragon','dark','fairy']
def eff(atk, deftypes):
    m=1.0
    for t in deftypes:
        if t and t!='none': m*=teff[atk][TYPES.index(t)]
    return m
pvmoves={m['moveId']:m for m in PV['moves']}
ALIAS={'FUTURE_SIGHT':'FUTURESIGHT'}
def pve(mid, fast):
    if mid.endswith('_PLUS'): return None
    if mid.startswith('HIDDEN_POWER_') and fast:
        b=ms.get('HIDDEN_POWER_FAST'); 
        if not b: return None
        return dict(type=mid[13:].lower(), power=b['power'], energy=b.get('energyDelta',0), dur=b['durationMs']/1000)
    for k in ([mid+'_FAST',mid] if fast else [ALIAS.get(mid,mid), mid]):
        if k in ms:
            s=ms[k]; return dict(type=s['pokemonType'].replace('POKEMON_TYPE_','').lower(), power=s.get('power',0), energy=s.get('energyDelta',0), dur=s['durationMs']/1000)
    return None
CPM=0.7903
EXTRA={'kingambit':['KOWTOW_CLEAVE']}
def calc(atk_b,def_b,hp_b,types,shadow,mega,F,C,tdef=160.0,dtypes=None):
    A=(atk_b+15)*CPM*(1.2 if shadow else 1); D=(def_b+15)*CPM*(5/6 if shadow else 1); HP=math.floor((hp_b+15)*CPM)
    y=900.0/D
    def dmg(m):
        stab=1.2 if m['type'] in types else 1
        boost=(1.3 if m['type'] in types else 1.1) if mega else 1
        e=eff(m['type'],dtypes) if dtypes else 1
        return math.floor(0.5*m['power']*A/tdef*stab*boost*e)+1
    FD=dmg(F); FE=F['energy']; Fd=F['dur']
    CD=dmg(C); CE=-C['energy']; Cd=C['dur']
    if FE<=0 or CE<=0: return None
    if CE>=100: CE=CE+0.5*FE+0.5*y*Cd
    FDPS=FD/Fd; FEPS=FE/Fd; CDPS=CD/Cd; CEPS=CE/Cd
    x=0.5*CE+0.5*FE
    if CDPS>FDPS:
        dps=(FDPS*CEPS+CDPS*FEPS)/(CEPS+FEPS)+(CDPS-FDPS)/(CEPS+FEPS)*(0.5-x/HP)*y
    else: dps=FDPS
    dps=max(dps,FDPS*0.5)
    tdo=dps*HP/y
    return dps,tdo
def label(e):
    tags=e.get('tags',[])
    if 'shadow' in tags: return 'shadow'
    if 'mega' in tags: return 'primal' if 'primal' in e['speciesId'] else 'mega'
    return ''
rows=[]
skipped=set()
for e in PV['pokemon']:
    if not e.get('released'): continue
    tags=e.get('tags',[])
    if 'duplicate' in tags or 'duplicate1500' in tags: continue
    sid=e['speciesId']
    if sid.endswith('_xs') or sid.endswith('_xl'): continue
    types=[t for t in e['types'] if t!='none']
    kind=label(e); shadow=kind=='shadow'; mega=kind in('mega','primal')
    fast=[(m,pve(m,True)) for m in e['fastMoves']]
    base=sid.replace('_shadow','')
    ch=[(m,pve(m,False)) for m in e['chargedMoves']+EXTRA.get(base,[])]
    for m,p in fast+ch:
        if p is None: skipped.add(m)
    fast=[(m,p) for m,p in fast if p]; ch=[(m,p) for m,p in ch if p]
    elite=set(e.get('eliteMoves',[])+e.get('legacyMoves',[])+(['KOWTOW_CLEAVE'] if base=='kingambit' else []))
    rows.append(dict(e=e,types=types,kind=kind,shadow=shadow,mega=mega,fast=fast,ch=ch,elite=elite))
def nm(mid,elite):
    n=pvmoves.get(mid,{}).get('name',mid.title().replace('_',' '))
    return n+('*' if mid in elite else '')
def best(r, dtypes=None, tdef=160.0, only=None):
    b=None; bs=r['e']['baseStats']
    for fm,F in r['fast']:
        for cm,C in r['ch']:
            if only and not (F['type']==only and C['type']==only): continue
            res=calc(bs['atk'],bs['def'],bs['hp'],r['types'],r['shadow'],r['mega'],F,C,tdef,dtypes)
            if not res: continue
            if b is None or res[0]>b[0]: b=(res[0],res[1],fm,cm,F['type'],C['type'])
    return b
if __name__=='__main__':
    print('skipped moves', sorted(skipped))
    out=[]
    for r in rows:
        b=best(r)
        if b: out.append((b[0],r['e']['speciesName'],nm(b[2],r['elite']),nm(b[3],r['elite']),b[1]))
    out.sort(reverse=True)
    for o in out[:30]: print('%.2f %-35s %s / %s  tdo %.0f'%o)
    print(len(rows))
