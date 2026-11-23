#!/bin/sh
# Stáhne herní data a žebříčky PvPoke do src/gm/ (spouštěj ze složky src/).
set -e
mkdir -p gm/rank
GH=https://raw.githubusercontent.com
curl -fsSL -o gm/alex.json   $GH/alexelgt/game_masters/master/GAME_MASTER.json
curl -fsSL -o gm/pvpoke.json $GH/pvpoke/pvpoke/master/src/data/gamemaster.json
for cp in 1500 2500 10000; do
  curl -fsSL -o gm/rank/r$cp.json $GH/pvpoke/pvpoke/master/src/data/rankings/all/overall/rankings-$cp.json
  curl -fsSL -o gm/rank/m$cp.json $GH/pvpoke/pvpoke/master/src/data/rankings/mega/overall/rankings-$cp.json
done
curl -fsSL -o gm/sd_events.json $GH/bigfoott/ScrapedDuck/data/events.min.json
curl -fsSL -o gm/sd_raids.json  $GH/bigfoott/ScrapedDuck/data/raids.min.json
echo fetched
