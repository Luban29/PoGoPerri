# PoGo Kompas

Tahák na Pokémon GO: co se tento týden děje, raid countery na aktuální bosse, Damage meter s DPS všech Pokémonů
(včetně Shadow, Mega/Primal a Mega+ útoků) a PvP žebříček.

## Jak je projekt poskládaný

- `docs/index.html` je hotový web. GitHub Pages ho servíruje z větve `main`, složky `/docs`.
- `docs/data/dm.json` – Damage meter (jeden Pokémon na řádek), `docs/data/counters.json` – countery na aktuální 5★ bosse.
- `src/` – výpočet DPS/TDO (`dps.py`), staty Mega+ útoků (`plus.py`) a skript, který zapíše data (`build_data.py`).

## Aktualizace dat

1. Stáhni herní data do `src/gm/`:
   - `alex.json` z `https://raw.githubusercontent.com/alexelgt/game_masters/master/GAME_MASTER.json` (PvE útoky)
   - `pvpoke.json` z `https://raw.githubusercontent.com/pvpoke/pvpoke/master/src/data/gamemaster.json` (Pokémoni a movepooly)
2. Nové Mega+ útoky doplň do `src/plus.py`, nové bosse do `bosses` v `src/build_data.py` a do `BOSSES` v `docs/index.html`.
3. `cd src && python3 build_data.py` zapíše `dm.json` a `counters.json`; zkopíruj je do `docs/data/`.
4. Týdenní obsah (Tento týden, Co dělat, PvP) je přímo v `docs/index.html` (`EVENTS`, `TODOS`, `LEAGUES`).

## Výpočet

Level 40, IV 15/15/15, cíl s Def 160 (u bossů jejich skutečná Def), bez počasí. Shadow ×1,2 útok / ×5/6 obrana,
Mega/Primal 1,3× na vlastní typ a 1,1× ostatní, Mega+ útoky podle Mega úrovně (×1,0 / 1,1 / 1,2 / 1,3).
DPS podle „comprehensive DPS“ vzorce, skóre = (DPS³·TDO)^¼.

Fanouškovský projekt, není spojený s Niantic, Scopely ani The Pokémon Company.
