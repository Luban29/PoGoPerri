from dps import *
from plus import PLUS, LVL
import json
def ok(m): return not m.startswith('HIDDEN_POWER')
for r in rows:
    r['fast']=[(m,p) for m,p in r['fast'] if ok(m)]
    r['plus']=PLUS.get(r['e']['speciesId'])
def charged(r,L):
    ch=list(r['ch'])
    if r['plus']:
        mid,name,t,pw,dur=r['plus']
        ch.append((mid,dict(type=t,power=pw*LVL[L],energy=-100,dur=dur),name))
    return ch
def mname(item,elite):
    return item[2] if len(item)>2 else nm(item[0],elite)
def bestf(r,L=4,dtypes=None,tdef=160.0,only=None,se=False):
    b=None; bs=r['e']['baseStats']
    for fm,F in r['fast']:
        for it in charged(r,L):
            C=it[1]
            if only and not (F['type']==only and C['type']==only): continue
            if se and eff(C['type'],dtypes)<=1: continue
            res=calc(bs['atk'],bs['def'],bs['hp'],r['types'],r['shadow'],r['mega'],F,C,tdef,dtypes)
            if not res: continue
            if b is None or res[0]>b[0]: b=(res[0],res[1],nm(fm,r['elite']),mname(it,r['elite']),F['type'],C['type'])
    return b
def entries(r,L):
    ent=[]
    b=bestf(r,L)
    if not b: return None
    ent.append(['all',round(b[0],2),round(b[1]),b[2],b[3],b[4],b[5]])
    for t in TYPES:
        bt=bestf(r,L,only=t)
        if bt: ent.append([t,round(bt[0],2),round(bt[1]),bt[2],bt[3],t,t])
    return ent
dm=[]
for r in rows:
    e4=entries(r,4)
    if not e4: continue
    row=[r['e']['speciesName'],r['kind'],r['types'],e4]
    if r['plus']: row.append({str(L):entries(r,L) for L in (1,2,3)})
    dm.append(row)
open('../docs/data/dm.json','w').write('[\n'+',\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in dm)+'\n]\n')
print(len(dm), len(json.dumps(dm,separators=(',',':'))))
bosses={'darkrai':(198,['dark']),'cresselia':(228,['psychic'])}
co={}
for k,(bdef,bt) in bosses.items():
    tdef=(bdef+15)*0.79; co[k]={}
    for L in (1,2,3,4):
        out=[]
        for r in rows:
            b=bestf(r,L,dtypes=bt,tdef=tdef,se=True)
            if b: out.append(dict(score=round((b[0]**3*b[1])**0.25,1),dps=round(b[0],1),tdo=round(b[1]),name=r['e']['speciesName'],fast=b[2],charged=b[3],ctype=b[5],kind=r['kind']))
        out.sort(key=lambda o:-o['score'])
        co[k][str(L)]={'all':out[:10],'nomega':[o for o in out if o['kind'] not in ('mega','primal')][:10],'plain':[o for o in out if not o['kind']][:10]}
    print(k,'L4'); [print('  ',o['name'],o['fast'],o['charged'],o['dps'],o['score']) for o in co[k]['4']['all']]
json.dump(co,open('../docs/data/counters.json','w'),ensure_ascii=False,separators=(',',':'))
# overall top at L4 and L1
for L in (1,4):
    top=sorted([(m[3][0][1],m[0],m[3][0][3],m[3][0][4]) for m in dm] if L==4 else [((m[4]['1'][0][1] if len(m)>4 else m[3][0][1]),m[0],(m[4]['1'][0][4] if len(m)>4 else m[3][0][4]),'') for m in dm],reverse=True)[:12]
    print('L',L,top)
