# PoGo Kompas

Tahák na Pokémon GO: co se tento týden děje, raid countery na aktuální bosse, Damage meter s DPS všech Pokémonů
(včetně Shadow, Mega/Primal a Mega+ útoků) a PvP žebříček.

## Jak je projekt poskládaný

- `docs/index.html` je hotový web. GitHub Pages ho servíruje z větve `main`, složky `/docs`.
- `docs/data/dm.json` – Damage meter (jeden Pokémon na řádek), `docs/data/counters.json` – countery na aktuální 5★ bosse.
- `src/` – výpočet DPS/TDO (`dps.py`), staty Mega+ útoků (`plus.py`) a skript, který zapíše data (`build_data.py`).

## Automatická aktualizace

GitHub Actions (`.github/workflows/update.yml`) každý den v 5:17 SEČ spustí `src/fetch.sh` (game master, PvPoke žebříčky,
ScrapedDuck = data z Leek Duck), přepočítá všechna data a změny nahraje. `src/auto.py` přitom doplní raid bosse a Max Monday bosse,
kteří v ručním seznamu chybí, ukončí ty, kteří už v raidech nejsou, a přidá nové eventy jen s názvem, časem a odkazem
(položky s `"auto": 1`). České popisy eventů, tipy a ruční seznamy v `bosses.py` a `events.py` doplňuje jednou týdně Claude.
Ručně jde běh spustit na GitHubu v záložce Actions → Denní aktualizace dat → Run workflow.

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

## PvP žebříček

`cd src && python3 build_pvp.py` zapíše `docs/data/pvp.json` (top 100 pro Great, Ultra a Master League).
Potřebuje navíc žebříčky PvPoke v `src/gm/rank/`: `r1500.json`, `r2500.json`, `r10000.json` z
`https://raw.githubusercontent.com/pvpoke/pvpoke/master/src/data/rankings/all/overall/rankings-<CP>.json`.
Detail Pokémona má vlastní adresu `#pvp-<liga>-<speciesId>`, např. `#pvp-great-medicham`.

## Detail Pokémona v Raidech a Damage meteru

`build_data.py` zapíše i `docs/data/pve.json` (movepooly, base staty, PvE hodnoty útoků a tabulka typů).
Movesety v detailu počítá prohlížeč stejným vzorcem jako `dps.py`, takže reagují na Mega úroveň.
Adresy: `#dmg-<speciesId>` (neutrální cíl) a `#raid-<boss>-<speciesId>` (proti bossovi).

## Události

`cd src && python3 events.py` zapíše `docs/data/events.json`: všechny eventy (s bonusy, shiny, úkoly a odměnami),
promokódy, partnerské akce a týdenní rytmus. Stránka sama třídí na Právě běží / Brzy / Do budoucna podle aktuálního času.
Detail eventu má adresu `#udalost-<id>`. Časy jsou místní, GBL a Global Challenge přepočtené na SEČ.

### Megy a Primaly v PvP

`build_pvp.py` čte i žebříčky Mega Edition (`src/gm/rank/m1500.json`, `m2500.json`, `m10000.json` z
`.../rankings/mega/overall/rankings-<CP>.json`) a z nich bere všechny Mega a Primal formy (klíče `megagreat`, `megaultra`, `megamaster`).
Detail: `#pvp-megagreat-sableye_mega`.

## Raidy a Max Battles

`cd src && python3 bosses.py` zapíše `docs/data/bosses.json`: aktuální raid bosse všech tierů (1★, 3★, 5★, Mega, Shadow 1★/3★/5★)
s daty, Max Battle bosse a seznam Dynamax/Gigantamax Pokémonů. Countery počítá prohlížeč z `pve.json` (stejný vzorec jako `dps.py`),
takže stačí upravit seznam bossů. Detail counteru: `#raid-<tier><bossId bez _>-<speciesId>`, např. `#raid-5darkrai-lucario_mega`.
