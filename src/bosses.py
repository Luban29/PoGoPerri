# Aktuální raid bossové, Max Battle bossové a seznam Dynamax/Gigantamax Pokémonů -> docs/data/bosses.json
# Zdroje: Pokémon GO Hub (Current Raid Bosses, 15. 11. 2026), Leek Duck (Twilight Wishes, Deoxys, Mega Metagross,
# Dynamax Trails), GO Hub DB a godex.site/maxdex (seznam Dynamax a Gigantamax Pokémonů).
# Zacian (Crowned Sword), Zamazenta (Crowned Shield) a Eternatus mají v Max Battles pevný Max útok (viz FIXED v index.html).
import json, re
pve = json.load(open('../docs/data/pve.json')); IDS = {m[0]: m for m in pve['mons']}

NOW = ('2026-11-16T06:00', '2026-11-24T22:00')
NEXT = ('2026-11-24T10:00', '2026-12-01T22:00')
RAIDS = [
  # tier, id, from, to, label (optional)
  ('5', 'darkrai', '2026-11-09T06:00', '2026-11-25T06:00'), ('5', 'cresselia', '2026-11-09T06:00', '2026-11-25T06:00'),
  ('5', 'deoxys', '2026-11-25T06:00', '2026-12-01T22:00'), ('5', 'deoxys_attack', '2026-11-25T06:00', '2026-12-01T22:00'),
  ('5', 'deoxys_defense', '2026-11-25T06:00', '2026-12-01T22:00'), ('5', 'deoxys_speed', '2026-11-25T06:00', '2026-12-01T22:00'),
  ('mega', 'banette_mega', '2026-11-16T06:00', '2026-11-24T22:00'),
  ('mega', 'beedrill_mega', '2026-11-24T10:00', '2026-11-30T20:00'), ('mega', 'houndoom_mega', '2026-11-24T10:00', '2026-11-30T20:00'),
  ('mega', 'sableye_mega', '2026-11-24T10:00', '2026-11-30T20:00'), ('mega', 'manectric_mega', '2026-11-24T10:00', '2026-11-30T20:00'),
  ('mega', 'metagross_mega', '2026-11-25T06:00', '2026-12-01T22:00'),
  ('s5', 'tornadus_incarnate', '2026-11-16T06:00', '2026-12-01T22:00', 'Shadow Tornadus (Incarnate)'),
  ('3', 'marowak_alolan', *NOW), ('3', 'liepard', *NOW), ('3', 'golurk', *NOW),
  ('3', 'espeon', '2026-11-24T10:00', '2026-11-30T20:00', 'Espeon (sun scarf)'), ('3', 'umbreon', '2026-11-24T10:00', '2026-11-30T20:00', 'Umbreon (moon scarf)'),
  ('s3', 'prinplup', *NOW, 'Shadow Prinplup'), ('s3', 'piloswine', *NOW, 'Shadow Piloswine'), ('s3', 'poliwhirl', *NOW, 'Shadow Poliwhirl'),
  ('1', 'meowth_alolan', *NOW), ('1', 'misdreavus', *NOW), ('1', 'yamask', *NOW), ('1', 'sandygast', *NOW),
  ('1', 'pikachu', '2026-11-24T10:00', '2026-11-30T20:00', 'Pikachu (sun crown)'), ('1', 'pikachu', '2026-11-24T10:00', '2026-11-30T20:00', 'Pikachu (moon crown)'),
  ('s1', 'larvitar', *NOW, 'Shadow Larvitar'), ('s1', 'mudkip', *NOW, 'Shadow Mudkip'), ('s1', 'makuhita', *NOW, 'Shadow Makuhita'), ('s1', 'cranidos', *NOW, 'Shadow Cranidos'),
]
MAX = [
  # tier label, id, from, to, name, note
  ('6★ Eternamax', 'eternatus', '2026-11-21T11:00', '2026-11-21T14:00', 'Eternamax Eternatus', 'Nejde chytit, odměnou jsou Eternatus Candy a XL. Countery počítané podle typů Eternatuse (Poison/Dragon).'),
  ('Max Monday', 'espurr', '2026-11-23T06:00', '2026-11-29T21:00', 'Dynamax Espurr', 'Týdenní Max Battles 23.–29. 11.'),
  ('Max Battles', 'cryogonal', '2026-11-30T06:00', '2026-12-06T21:00', 'Dynamax Cryogonal', 'Týdenní Max Battles 30. 11. – 6. 12.'),
]
DMAX_NAMES = """Dynamax Bulbasaur, Dynamax Ivysaur, Dynamax Venusaur, Gigantamax Venusaur, Dynamax Charmander, Dynamax Charmeleon, Dynamax Charizard, Gigantamax Charizard, Dynamax Squirtle, Dynamax Wartortle, Dynamax Blastoise, Gigantamax Blastoise, Dynamax Caterpie, Dynamax Metapod, Dynamax Butterfree, Gigantamax Butterfree, Gigantamax Meowth, Dynamax Growlithe, Dynamax Arcanine, Dynamax Abra, Dynamax Kadabra, Dynamax Alakazam, Dynamax Machop, Dynamax Machoke, Dynamax Machamp, Gigantamax Machamp, Dynamax Gastly, Dynamax Haunter, Dynamax Gengar, Gigantamax Gengar, Dynamax Krabby, Dynamax Kingler, Gigantamax Kingler, Dynamax Hitmonlee, Dynamax Hitmonchan, Dynamax Rhyhorn, Dynamax Rhydon, Dynamax Chansey, Dynamax Electabuzz, Dynamax Magikarp, Dynamax Gyarados, Dynamax Lapras, Gigantamax Lapras, Dynamax Eevee, Dynamax Vaporeon, Dynamax Jolteon, Dynamax Flareon, Dynamax Omanyte, Dynamax Omastar, Dynamax Kabuto, Dynamax Kabutops, Gigantamax Snorlax, Dynamax Articuno, Dynamax Zapdos, Dynamax Moltres, Dynamax Hoothoot, Dynamax Noctowl, Dynamax Espeon, Dynamax Umbreon, Dynamax Shuckle, Dynamax Sneasel, Dynamax Hitmontop, Dynamax Blissey, Dynamax Raikou, Dynamax Entei, Dynamax Suicune, Dynamax Lugia, Dynamax Ho-Oh, Dynamax Ralts, Dynamax Kirlia, Dynamax Gardevoir, Dynamax Sableye, Dynamax Wailmer, Dynamax Wailord, Dynamax Trapinch, Dynamax Vibrava, Dynamax Flygon, Dynamax Feebas, Dynamax Milotic, Dynamax Spheal, Dynamax Sealeo, Dynamax Walrein, Dynamax Beldum, Dynamax Metang, Dynamax Metagross, Dynamax Regirock, Dynamax Regice, Dynamax Registeel, Dynamax Latias, Dynamax Latios, Dynamax Weavile, Dynamax Rhyperior, Dynamax Electivire, Dynamax Leafeon, Dynamax Glaceon, Dynamax Gallade, Dynamax Uxie, Dynamax Mesprit, Dynamax Azelf, Dynamax Dialga, Dynamax Palkia, Dynamax Pidove, Dynamax Tranquill, Dynamax Unfezant, Dynamax Roggenrola, Dynamax Boldore, Dynamax Gigalith, Dynamax Woobat, Dynamax Swoobat, Dynamax Drilbur, Dynamax Excadrill, Dynamax Darumaka, Dynamax Darmanitan, Dynamax Trubbish, Dynamax Garbodor, Gigantamax Garbodor, Dynamax Cryogonal, Dynamax Deino, Dynamax Zweilous, Dynamax Hydreigon, Dynamax Inkay, Dynamax Malamar, Dynamax Sylveon, Dynamax Bounsweet, Dynamax Steenee, Dynamax Tsareena, Dynamax Passimian, Dynamax Drampa, Dynamax Meltan, Dynamax Melmetal, Gigantamax Melmetal, Dynamax Grookey, Dynamax Thwackey, Dynamax Rillaboom, Gigantamax Rillaboom, Dynamax Scorbunny, Dynamax Raboot, Dynamax Cinderace, Gigantamax Cinderace, Dynamax Sobble, Dynamax Drizzile, Dynamax Inteleon, Gigantamax Inteleon, Dynamax Skwovet, Dynamax Greedent, Dynamax Rookidee, Dynamax Corvisquire, Dynamax Corviknight, Dynamax Wooloo, Dynamax Dubwool, Dynamax Toxtricity (Amped Form), Dynamax Toxtricity (Low Key Form), Gigantamax Toxtricity, Dynamax Sizzlipede, Dynamax Centiskorch, Dynamax Hatenna, Dynamax Hattrem, Dynamax Hatterene, Gigantamax Grimmsnarl, Dynamax Falinks, Dynamax Duraludon, Gigantamax Duraludon, Dynamax Kubfu, Dynamax Urshifu (Rapid Strike Style), Dynamax Urshifu (Single Strike Style), Dynamax Regidrago, Dynamax Pikachu, Gigantamax Pikachu, Dynamax Raichu, Dynamax Magmar, Dynamax Magmortar, Dynamax Combee, Dynamax Vespiquen, Dynamax Cottonee, Dynamax Whimsicott, Dynamax Zacian (Crowned Sword), Dynamax Zamazenta (Crowned Shield), Dynamax Eternatus"""
FIX = {'ho-oh': 'ho_oh', 'toxtricity (amped form)': 'toxtricity', 'toxtricity (low key form)': 'toxtricity', 'toxtricity': 'toxtricity',
       'urshifu (rapid strike style)': 'urshifu_rapid_strike', 'urshifu (single strike style)': 'urshifu_single_strike',
       'darmanitan': 'darmanitan_standard', 'meowth': 'meowth',
       'zacian (crowned sword)': 'zacian_crowned_sword', 'zamazenta (crowned shield)': 'zamazenta_crowned_shield'}
dmax = {}
for n in [x.strip() for x in DMAX_NAMES.split(',')]:
    g = n.startswith('Gigantamax'); base = n.split(' ', 1)[1].lower()
    sid = FIX.get(base, base.replace(' ', '_').replace('-', '_').replace('.', ''))
    if sid not in IDS:
        print('MISSING', n, sid); continue
    dmax[sid] = max(dmax.get(sid, 0), 1 if g else 0)
raids = []
for r in RAIDS:
    tier, sid, a, b = r[:4]
    assert sid in IDS, sid
    raids.append({'t': tier, 'id': sid, 'n': r[4] if len(r) > 4 else IDS[sid][1], 'a': a, 'b': b})
mx = []
for t, sid, a, b, n, note in MAX:
    assert sid in IDS, sid
    mx.append({'t': t, 'id': sid, 'n': n, 'a': a, 'b': b, 'note': note})
json.dump({'raids': raids, 'max': mx, 'dmax': [[k, v] for k, v in sorted(dmax.items())]}, open('../docs/data/bosses.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(raids), 'raid bosses,', len(mx), 'max,', len(dmax), 'dynamax attackers (', sum(dmax.values()), 'G-Max )')
