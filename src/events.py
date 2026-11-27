# Události pro záložku "Události" -> docs/data/events.json
# Časy jsou místní (jak je udává hra), u GO Battle League a Global Challenge přepočtené z PT/PST na SEČ.
# Zdroje: Leek Duck, pokemongo.com, Pokémon GO Hub, Dittobase (stav k 27. 11. 2026).
import json

SPAWNS_DYNAMAX = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Pikachu", "Growlithe", "Abra", "Machop", "Gastly", "Krabby",
    "Hitmonlee", "Hitmonchan", "Rhyhorn", "Chansey", "Electabuzz", "Magmar", "Magikarp", "Eevee", "Omanyte", "Kabuto", "Hoothoot",
    "Shuckle", "Sneasel", "Hitmontop", "Ralts", "Sableye", "Wailmer", "Trapinch", "Feebas", "Spheal", "Beldum", "Combee", "Pidove",
    "Roggenrola", "Woobat", "Drilbur", "Cottonee", "Darumaka", "Trubbish", "Cryogonal", "Deino", "Inkay", "Bounsweet", "Passimian",
    "Drampa", "Grookey", "Scorbunny", "Sobble", "Skwovet", "Rookidee", "Wooloo", "Toxtricity (Amped)", "Toxtricity (Low Key)",
    "Sizzlipede", "Hatenna", "Falinks", "Duraludon"]

E = []
def ev(**k): E.append(k)

# ---------------- PRÁVĚ BĚŽÍ / TENTO TÝDEN ----------------
ev(id="dynamax-trails", cat="event", title="Dynamax Trails", start="2026-11-16T10:00", end="2026-11-23T20:00",
   summary="Týden Max Battles: víc Power Spotů, Dynamax Pokémoni ve volné přírodě a návrat Eternatuse přes GO Pass.",
   sections=[
     dict(h="Bonusy", list=[
       "Víc aktivních Power Spotů než obvykle.",
       "Chycení eventového Pokémona ve volné přírodě nebo po Max Battle má šanci dát 10 Max Particles (počítá se i po dosažení denního limitu 800). Neplatí pro Explorer Gadget a GO Plus+.",
       "Úspěšné chycení Pokémona z Max Battle má šanci na Special Background.",
       "Remote Raid limit 30 místo 10: 20. 11. 22:00 – 22. 11. 3:00 (SEČ)."]),
     dict(h="Ve volné přírodě a v Max Battles", mons=[[m, 1] for m in SPAWNS_DYNAMAX],
          note="Max Battles: všichni dosud vydaní Dynamax Pokémoni kromě legendárních a mýtických."),
     dict(h="Spotlight Hour · čt 19. 11. 18–19", mons=[["Grookey", 1], ["Scorbunny", 1], ["Sobble", 1]], note="Bonus: 2× Catch Candy."),
     dict(h="Field Research", tasks=[
       ["Chyť 8 Pokémonů", "Bulbasaur, Charmander, Squirtle, Grookey, Scorbunny, Sobble a další"],
       ["Powerupni Pokémony 8×", "Magikarp, Feebas nebo 3× Pinap Berry"],
       ["Projdi 1 km", "Eevee nebo 2 000 Stardust"],
       ["Vyhraj Max Battle", "Drampa, Duraludon, 10 Eternatus Candy nebo 2 000 Stardust"],
       ["Odemkni Max Move", "25 Eternatus Candy nebo 5 000 Stardust"],
       ["Excellent Throw", "25 Eternatus Candy, Golden Razz nebo Silver Pinap"]]),
     dict(h="GO Pass: Dynamax Trails", list=[
       "Zdarma, dostaneš ho automaticky 16. 11. Deluxe stojí 4,99 USD (zdarma, pokud máš Rank 1 v GO Pass: Into the Wild a vyzvedl sis fialové tričko GO Wild Area).",
       "Body denně až 900: Max Battle 200, raid 100, vylíhnutí vajíčka 40, chycení 10. Denní úkol: 10× powerup (100 bodů).",
       "Hlavní odměna: Eternatus (pokud ho už máš, dostaneš 100 Eternatus Candy XL), Eternatus Candy a XL, Rare Candy, Dynamax encountery se Special Background.",
       "Milníky: Rank 15 = 2× Catch Stardust · Rank 35 = Dynamax Cannon za poloviční cenu · Rank 55 = +5 Candy a +3 XL za Max Battles.",
       "Body sbírej do 23. 11. 20:00, odměny vyzvedni do 25. 11. 20:00."]),
   ],
   src="https://leekduck.com/events/dynamax-trails-2026/")

ev(id="darkrai-cresselia", bosses=[["raid","5","darkrai"],["raid","5","cresselia"]], cat="raid", title="5★ raidy: Darkrai a Cresselia", start="2026-11-09T06:00", end="2026-11-25T06:00",
   summary="Legendární raidy, countery najdeš v záložce Raidy.",
   sections=[dict(h="Bossové", mons=[["Darkrai", 1], ["Cresselia", 1]]),
             dict(h="Tipy", list=["Darkrai je slabý na Fighting, Bug a Fairy.", "Cresselia je slabá na Bug, Ghost a Dark.", "Raid Hour byla ve středu 18. 11. 18–19."]),
             dict(h="Countery", link=["raidy", "Otevřít countery v záložce Raidy"])],
   src="https://pokemongohub.net/post/event/pokemon-go-november-2026-events/")

ev(id="mega-banette", bosses=[["raid","mega","banette_mega"]], cat="raid", title="Mega Banette v Mega raidech", start="2026-11-16T06:00", end="2026-11-24T22:00",
   summary="Ghost Mega boss, slabý na Dark a Ghost útoky.", sections=[dict(h="Boss", mons=[["Mega Banette", 1]])],
   src="https://pokemongohub.net/post/event/this-week-in-pokemon-go-november-16-22-dynamax-trails-eternatus-pawniard-community-day/")

ev(id="shadow-tornadus", cat="raid", title="Shadow Tornadus ve Shadow raidech", start="2026-11-16T06:00", end="2026-12-01T22:00",
   summary="5★ Shadow raidy o víkendech (Incarnate forma).", sections=[dict(h="Boss", mons=[["Shadow Tornadus (Incarnate)", 0]],
   note="5★ Shadow raidy jsou jen o víkendech. Na létajícího bosse ber Electric, Ice nebo Rock útočníky a Purified Gems.")],
   src="https://leekduck.com/events/shadow-tornadus-incarnate-forme-in-shadow-raids-november-16-2026/")

ev(id="gbl-1", cat="gbl", title="GBL: Ultra, Master: Mega Edition, GO LAIC Cup", start="2026-11-18T22:00", end="2026-11-25T22:00",
   summary="4× Stardust za výhry (kromě odměn za konec setu).",
   sections=[dict(h="Ligy", list=["Ultra League (max 2 500 CP)", "Master League: Mega Edition (Mega Pokémoni povoleni)",
     "2026 GO LAIC Cup: max 1 500 CP, bez Fire, Dark, Steel a Fairy typů, bez legendárních, mýtických a Ultra Beasts, bez Mega"]),
     dict(h="Žebříčky", link=["pvp", "Otevřít PvP žebříček"])],
   src="https://leekduck.com/events/gbl-twilight-trails_ultra-league_master-league-mega-edition_2026-go-laic-cup/")

ev(id="duolingo", cat="partner", title="Duolingo × Pokémon GO", start="2026-11-17T02:00", end="2026-12-31T23:59",
   summary="Uč se 7 dní v Duolingu a dostaneš kód na Timed Research s Pikachu, Meowthem, Chatotem a Lucariem.",
   sections=[dict(h="Jak na to", list=["V Duolingu se připoj do questu Duo’s Pokémon Party (do 21. 12.).",
       "Dej aspoň jednu lekci denně v 7 různých dnech (do 29. 12.).",
       "Kód (každý má vlastní) uplatni ve Web Storu: store.pokemongo.com/offer-redemption."]),
     dict(h="Odměny v Pokémon GO", mons=[["Pikachu", 1], ["Meowth", 1], ["Chatot", 1], ["Lucario", 1]],
          note="Všichni se Special Background. Úkoly jsou v jazyce, který si vybereš s profesorkou Willow. Dále XP a Stardust. Dokončit do 31. 12. 23:59."),
     dict(h="V Duolingu", list=["Až 4 Pokémon kostýmy pro avatara v Duolingu."])],
   src="https://leekduck.com/events/duolingo-timed-research-2026/")

ev(id="adidas", cat="partner", title="adidas × Pokémon", start="2026-09-25T00:00", end="2027-01-15T23:59",
   summary="Kód ADIDASxPOKEMON na boty pro avatara + Timed Research v prodejnách adidas.",
   sections=[dict(h="Promokód", codes=[["ADIDASxPOKEMON", "Boty adidas pro avatara", "do 15. 1. 2027"]]),
     dict(h="Timed Research v obchodě", list=["Navštiv zúčastněnou prodejnu adidas a otevři Pokémon GO (25. 9. 2026 – 15. 1. 2027).",
       "Odměny: bunda a kšiltovka adidas Pokémon pro avatara, XP, Stardust, Lucario a Lucario Mega Energy."])],
   src="https://pokemongo.com/en/news/pokemon-x-adidas-2026")

ev(id="crocs", cat="partner", title="Crocs × Pokémon", start="2026-11-16T00:00", end="2027-12-31T23:59",
   summary="Pikachu Crocs pro avatara zdarma, Gengar a Jigglypuff ke koupi skutečných bot.",
   sections=[dict(h="Promokódy", codes=[["POKEMONGOxCROCSxELECTRIFYING", "Pikachu Classic Clog", "do 31. 12. 2027"],
       ["POKEMONGOxCROCSxENCHANTING", "Gengar Classic Clog (oficiálně ke koupi Crocs)", "do 31. 12. 2027"],
       ["POKEMONGOxCROCSxMELODY", "Jigglypuff Classic Platform Clog (oficiálně ke koupi Crocs)", "do 31. 12. 2027"]])],
   src="https://pokemongo.com/news/pokemon-crocs-2026")

ev(id="max-mondays", cat="max", title="Max Mondays", start="2026-11-23T06:00", end="2026-11-30T21:00",
   summary="Každé pondělí 6–21: víc Power Spotů a 1 Rare Candy XL za každou osobní Max Battle.",
   sections=[dict(h="Termíny", list=["Po 23. 11. 6:00–21:00", "Po 30. 11. 6:00–21:00"]),
     dict(h="Max Battles během týdne", list=["23.–29. 11.: Dynamax Espurr", "30. 11. – 6. 12.: Dynamax Cryogonal"])],
   src="https://pokemongohub.net/post/event/pokemon-go-november-2026-events/")

# ---------------- BRZY ----------------
ev(id="twilight-wishes", cat="event", title="Twilight Wishes", start="2026-11-24T10:00", end="2026-11-30T20:00", featured=1,
   summary="Finále sezóny: Espeon a Umbreon v šálách a Pikachu v korunkách.",
   sections=[
     dict(h="Bonusy", list=["GO Pass Rank 1: vyšší šance na Lucky Trade a Lucky Friends.",
       "GO Pass Rank 10: 2× Stardust za chycení (s Deluxe 3×)."]),
     dict(h="Ve volné přírodě", mons=[["Clefairy", 0], ["Staryu", 1], ["Elgyem", 1], ["Rockruff", 1], ["Espeon (sun scarf)", 1], ["Umbreon (moon scarf)", 1]],
          note="Rockruff je vzácný."),
     dict(h="Raidy", groups=[["1★", [["Pikachu (sun crown)", 0], ["Pikachu (moon crown)", 0]]],
                            ["3★", [["Espeon (sun scarf)", 1], ["Umbreon (moon scarf)", 1]]],
                            ["Mega", [["Mega Beedrill", 1], ["Mega Houndoom", 1], ["Mega Sableye", 1], ["Mega Manectric", 1]]]]),
     dict(h="Field Research", list=["Odměny: Mega Energy a eventoví Pokémoni včetně Staryu a Elgyem.",
       "24. 11. 10:00 – 26. 11. 10:00: navíc Applin a Maschiff.",
       "26. 11. 10:00 – 30. 11. 20:00: navíc Gengar (Spooky Festival kostým), Drifblim (Halloween Mischief kostým) a Bramblin."]),
     dict(h="GO Pass: Twilight Wishes", list=["Zdarma: eventoví Pokémoni, Star Piece, Rare Candy, Mega Energy pro Beedrilla, Houndooma, Sableyeho a Manectrica.",
       "Deluxe 4,99 USD: víc encounterů, póza pro avatara, Star Pieces, Premium Battle Passy. Deluxe + 6 ranků 6,99 USD.",
       "Odměny vyzvedni do st 2. 12. 20:00."]),
   ], src="https://leekduck.com/events/twilight-wishes-2026/")

ev(id="gbl-2", cat="gbl", title="GBL: Master League a Mega Catch Cup: Great League Edition", start="2026-11-24T22:00", end="2026-12-01T22:00",
   summary="Poslední GBL týden sezóny, 4× Stardust za výhry.",
   sections=[dict(h="Ligy", list=["Master League", "Mega Catch Cup: Great League Edition (Pokémoni chycení od 8. 9. 2026, bez mýtických)"]),
             dict(h="Bonus", list=["4× Stardust za výhry (ne za konec setu)."])],
   src="https://leekduck.com/events/gbl-twilight-trails_master-league_mega-catch-cup-great-league-edition/")

ev(id="deoxys", bosses=[["raid","5","deoxys"],["raid","5","deoxys_attack"],["raid","5","deoxys_defense"],["raid","5","deoxys_speed"]], cat="raid", title="5★ raidy: Deoxys (všechny formy)", start="2026-11-25T06:00", end="2026-12-01T22:00",
   summary="Normal, Attack, Defense a Speed Deoxys. Raid Hour st 25. 11. 18–19.",
   sections=[dict(h="Bossové", mons=[["Deoxys (Normal)", 1], ["Deoxys (Attack)", 1], ["Deoxys (Defense)", 1], ["Deoxys (Speed)", 1]]),
             dict(h="Raid Hour", list=["Středa 25. 11. 18:00–19:00"])],
   src="https://leekduck.com/events/deoxys-normal-defense-attack-speed-formes-in-5-star-raid-battles-november-2026/")

ev(id="mega-metagross", bosses=[["raid","mega","metagross_mega"]], cat="raid", title="Mega Metagross v Mega raidech", start="2026-11-25T06:00", end="2026-12-01T22:00",
   summary="Mega Metagross v Mega raidech.", sections=[dict(h="Boss", mons=[["Mega Metagross", 1]])],
   src="https://leekduck.com/events/mega-metagross-in-mega-raids-november-2026/")

ev(id="spotlight-noibat", cat="spotlight", title="Spotlight Hour: Noibat", start="2026-11-26T18:00", end="2026-11-26T19:00",
   summary="Noibat ve velkém, bonus 2× Catch Candy.", sections=[dict(h="Pokémon", mons=[["Noibat", 1]], note="Bonus: 2× Catch Candy.")],
   src="https://pokemongohub.net/post/event/pokemon-go-november-2026-events/")

ev(id="clefable-smrd", bosses=[["raid","mega","clefable","Mega Clefable",["fairy","flying"],"Mega Clefable zatím není v herních datech, countery jsou spočítané na typy Fairy/Flying a statistiky běžného Clefable. Pořadí se po jejím přidání skoro nezmění."]], cat="raid", title="Clefable Super Mega Raid Day", start="2026-11-28T14:00", end="2026-11-28T17:00", featured=1,
   summary="Debut Mega Clefable a jejího Moonblast+, poprvé Super Max úroveň. Až 6 raid passů zdarma.",
   sections=[
     dict(h="Boss", mons=[["Mega Clefable", 1]], note="Clefable z těchto raidů má odemčenou Mega úroveň 1."),
     dict(h="Bonusy zdarma", list=["Až 6 raid passů zdarma z Photo Disců u Gymů.", "Remote Raid limit 20: pá 27. 11. 2:00 – ne 29. 11. 5:00 (SEČ)."]),
     dict(h="Ticket (4,99 USD)", list=["Až 14 raid passů z Gymů", "Vyšší šance na Rare Candy XL z raidů", "+5 000 XP a +5 000 Stardust za Super Mega raid",
       "Platí 14–17, jde darovat kamarádům od Great Friends. Ve Web Storu Ultra Ticket Box se stejnou cenou a Premium Battle Passem navíc."]),
     dict(h="Mega Clefable a Moonblast+", list=["Fairy/Flying, poprvé může dosáhnout Super Max úrovně (nejdřív Max, pak Clefable Mega Energy).",
       "Moonblast+: raidy 160, PvP 80 se šancí snížit útok soupeře. Síla roste s Mega úrovní."]),
     dict(h="Global Challenge", list=["Pá 27. 11. 2:00 – ne 29. 11. 5:00 (SEČ): plňte raidy s hráči z celého světa.",
       "Čím víc úrovní, tím silnější Moonblast+ (od Mega úrovně 1) a vyšší CP Clefable na Super Max. Bonus platí 30. 11. – 13. 12."]),
   ], src="https://leekduck.com/events/clefable-super-mega-raid-day-2026/")

ev(id="season-end", cat="event", title="Konec sezóny Twilight Trails", start="2026-12-01T00:00", end="2026-12-01T22:00",
   summary="Dotáhni sezónní výzkumy a GBL odměny, pak začíná nová sezóna.",
   sections=[dict(h="Co nestihnout zmeškat", list=["Konec GBL sezóny a odměn za rank.", "Shadow Tornadus, Deoxys a Mega Metagross končí 1. 12. 22:00."])],
   src="https://pokemongohub.net/post/event/pokemon-go-november-2026-events/")

# ---------------- PROSINEC (oznámeno 24.–25. 11.) ----------------
ev(id="daydream-destinations", cat="event", title="Nová sezóna: Daydream Destinations", start="2026-12-01T10:00", end="2027-03-01T10:00",
   summary="Sezóna do 1. 3. 2027: debut Mega Froslass a Mega Drampa, noví Dynamax Pokémoni a GO Tour: Alola v únoru.",
   sections=[
     dict(h="Sezónní GO Pass bonusy", list=["Rank 1: víc XP za zvýšení Friendship levelu a 2× Friendship bonus k damage v raidech.",
       "Rank 25: vyšší limity pro Photo Discy z PokéStopů a Gymů a pro dárky.", "Rank 50: 2× delší Daily Adventure Incense.",
       "Rank 75: víc XP a Stardust za líhnutí vajíček."]),
     dict(h="Debuty", list=["Pyukumuku (Tropical Paradise, 1.–7. 12.)", "Dvě nové formy Minior (Minior Showers: Geminids, 11.–16. 12.)",
       "Mega Froslass a Mega Drampa na vlastních Raid Days (data zatím neoznámena)",
       "Dynamax Alolan Sandshrew, Dynamax Slowpoke a Dynamax Corphish v Max Battles", "Gigantamax Inteleon (5. 12.), Gigantamax Toxtricity (datum zatím neoznámeno)"]),
     dict(h="Vajíčka", list=["2 km: Vulpix, Swablu, Yamper. Další vzdálenosti zatím nemáme ověřené."]),
     dict(h="Termíny", list=["Community Day: 12.–13. 12., 2. 1. (Classic), 16. 1., 6. 2.", "GO Tour: Alola – Global: 27.–28. 2. 2027",
       "GO Battle League: nová sezóna od 1. 12. 22:00 (SEČ), Mega ligy a cupy Holiday, Fighting, Jungle, Love a GO EUIC Cup."]),
     dict(h="Research Breakthrough", list=["Nová sada odměn za 7 razítek z Field Research. Pokémoni zatím nejsou oznámení."]),
   ], src="https://www.dexerto.com/pokemon/pokemon-go-daydream-destinations-season-guide-dates-events-raids-more-3431574/")

ev(id="tropical-paradise", cat="event", title="Tropical Paradise", start="2026-12-01T10:00", end="2026-12-07T20:00", featured=1,
   summary="Debut Pyukumuku ve 3★ raidech a Mega Slowbro poprvé na Super Max s novým Chilling Water+.",
   sections=[
     dict(h="Debut a nové útoky", list=["Pyukumuku: 3★ raidy a GO Pass. Umí nový rychlý útok Soak (síla 6 v raidech i PvP).",
       "Mega Slowbro může poprvé na Super Max úroveň: nejdřív Mega level 3, pak Slowbro Mega Energy.",
       "Chilling Water+ (nový nabitý útok Mega Slowbra): raidy 160, PvP 45 a jistě sníží útok soupeře. Síla roste s Mega úrovní."]),
     dict(h="Ve volné přírodě", mons=[["Slowpoke", 0], ["Shellder", 0], ["Wingull", 0], ["Slakoth", 0], ["Snorlax", 0]], note="Snorlax je vzácný."),
     dict(h="Navíc od pá 4. 12. 10:00", mons=[["Hoppip", 0], ["Lotad", 0], ["Shroomish", 0], ["Exeggutor (Alolan)", 0]], note="Alolan Exeggutor je vzácný."),
     dict(h="Raidy", groups=[["1★", [["Diglett (Alolan)", 0], ["Frillish", 0], ["Sandygast", 0]]], ["3★", [["Pyukumuku", 0]]]]),
     dict(h="Field Research", list=["Encountery s Psyduckem, Tentacoolem a Shellderem, u některých úkolů Slowbro Mega Energy."]),
     dict(h="GO Pass", list=["Rank 10: 2× XP z raidů.", "Rank 20: 5× Mega Energy za chození s Slowpokem, Slowbrem nebo Slowkingem jako buddy (po Mega evoluci Slowbra).",
       "Deluxe 4,99 USD (s +6 ranky 6,99 USD). Odměny vyzvedni do st 9. 12. 20:00."]),
   ], src="https://pokemongohub.net/post/event/pokemon-go-tropical-paradise-2026/")

ev(id="regidrago-dec", bosses=[["raid","5","regidrago"]], cat="raid", title="5★ raidy: Regidrago", start="2026-12-02T06:00", end="2026-12-08T22:00",
   summary="Regidrago v 5★ raidech, Raid Hour st 2. 12. 18–19.",
   sections=[dict(h="Boss", mons=[["Regidrago", 0]]), dict(h="Raid Hour", list=["Středa 2. 12. 18:00–19:00"])],
   src="https://leekduck.com/events/regidrago-in-5-star-raid-battles-december-2026/")

ev(id="mega-slowbro", bosses=[["raid","mega","slowbro_mega"]], cat="raid", title="Mega Slowbro v Mega raidech", start="2026-12-02T06:00", end="2026-12-08T22:00",
   summary="Mega Slowbro, od Tropical Paradise může na Super Max s Chilling Water+.", sections=[dict(h="Boss", mons=[["Mega Slowbro", 0]])],
   src="https://leekduck.com/events/mega-slowbro-in-mega-raids-december-2026/")

ev(id="shadow-dialga", bosses=[["raid","s5","dialga","Shadow Dialga"]], cat="raid", title="Shadow Dialga ve Shadow raidech", start="2026-12-02T06:00", end="2027-01-05T22:00",
   summary="Shadow Dialga ve Shadow raidech přes celý prosinec.", sections=[dict(h="Boss", mons=[["Shadow Dialga", 0]], note="Shadow raid: zuřícího bosse zklidníš Purified Gems.")],
   src="https://leekduck.com/events/shadow-dialga-in-shadow-raids-december-2026/")

ev(id="gbl-dd-1", cat="gbl", title="GBL: Great, Ultra a Master League: Mega Edition", start="2026-12-01T22:00", end="2026-12-08T22:00",
   summary="Start GBL sezóny Daydream Destinations, reset ranku.",
   sections=[dict(h="Ligy", list=["Great League: Mega Edition", "Ultra League: Mega Edition", "Master League: Mega Edition"]),
             dict(h="Pozor", list=["Nová sezóna začíná út 1. 12. 22:00 (SEČ), rank se resetuje. Odměny za Twilight Trails si vyzvedni předtím."])],
   src="https://pokemongohub.net/post/guide/gbl-daydream-destinations-update/")

ev(id="gbl-dd-2", cat="gbl", title="GBL: Great League: Mega Edition a Mountain Cup", start="2026-12-08T22:00", end="2026-12-15T22:00",
   summary="Great League: Mega Edition a Mountain Cup: Great League Edition.",
   sections=[dict(h="Ligy", list=["Great League: Mega Edition", "Mountain Cup: Great League Edition (pravidla cupu zatím nemáme ověřená)"])],
   src="https://pokemongohub.net/post/guide/gbl-daydream-destinations-update/")

ev(id="spotlight-wimpod", cat="spotlight", title="Spotlight Hour: Wimpod", start="2026-12-03T18:00", end="2026-12-03T19:00",
   summary="Wimpod ve velkém, bonus 2× Transfer Candy.", sections=[dict(h="Pokémon", mons=[["Wimpod", 0]], note="Bonus: 2× Transfer Candy.")],
   src="https://leekduck.com/events/pokemonspotlighthour2026-12-03/")

ev(id="inteleon-mbd", bosses=[["max","gmax","inteleon","Gigantamax Inteleon"]], cat="max", title="Gigantamax Inteleon Max Battle Day", start="2026-12-05T14:00", end="2026-12-05T17:00", featured=1,
   summary="Debut Gigantamax Inteleona v 6★ Max Battles, všechny Power Spoty s Gigantamaxem.",
   sections=[
     dict(h="Boss", mons=[["Gigantamax Inteleon", 0]], note="Water. Countery najdeš v záložce Max Battles (vyhledej „gmax inteleon“)."),
     dict(h="Bonusy 14–17", list=["Limit Max Particles 1 600", "Všechny Power Spoty hostí Gigantamax Battles, obnovují se častěji a je jich víc",
       "8× Max Particles z Power Spotů", "Až 3 Special Trades za den"]),
     dict(h="Bonusy 0–17", list=["2× Max Particles z prozkoumávání", "1/4 vzdálenost pro Max Particles (nejdřív vyber všechny v menu Nearby)"]),
     dict(h="Remote raidy", list=["Limit 20 místo 10: pá 4. 12. 1:00 – so 5. 12. 5:00 (SEČ)."]),
     dict(h="Ticket (4,99 USD)", list=["Timed Research: 1 Max Mushroom, 25 000 XP, 6 400 Max Particles", "2× XP z Max Battles 14–17",
       "V herním shopu do 17:00, jde darovat kamarádům od Great Friends. Ve Web Storu Ultra Ticket Box s 800 Max Particles navíc."]),
   ], src="https://pocketmonsters.net/news/9762")

ev(id="champions-celebration", bosses=[["raid","5","latias"],["raid","5","latios"],["raid","5","heatran"],["raid","5","cobalion"],["raid","5","terrakion"],["raid","5","virizion"],["raid","5","regieleki"],["raid","5","regidrago"]], cat="event", title="Pokémon Champions Celebration", start="2026-12-08T10:00", end="2026-12-14T20:00", featured=1,
   summary="Týden pro hráče Pokémon Champions: 8 legend v 5★ raidech se speciálním pozadím, Rare Candy z Field Research.",
   sections=[
     dict(h="Bonusy", list=["Vyšší šance na Kecleona u PokéStopů.", "GO Pass Rank 1: 7× GO Transporter Energy za hodinu (přesun do Pokémon HOME).",
       "Rank 10: 2× Catch Candy (nesčítá se s Community Day).", "Rank 20: +3 000 XP za raid, s Deluxe až 2 raid passy denně z Gymů.",
       "Pošli Pokémona přes HOME do Pokémon Champions a dostaneš dárek do Champions mailboxu."]),
     dict(h="Ve volné přírodě", mons=[["Charmander", 0], ["Starly", 0], ["Grookey", 0], ["Absol", 0], ["Gible", 0]], note="Seznam není úplný, další Pokémoni zatím neoznámeni."),
     dict(h="Raidy", groups=[["1★", [["Bagon", 0], ["Litten", 0], ["Frigibax", 0]]], ["3★", [["Raichu", 0], ["Garchomp", 0], ["Rillaboom", 0]]],
       ["5★ (9.–15. 12.)", [["Latias", 0], ["Latios", 0], ["Heatran", 0], ["Cobalion", 0], ["Terrakion", 0], ["Virizion", 0], ["Regieleki", 0], ["Regidrago", 0]]]]),
     dict(h="5★ raidy", list=["Legendy se střídají podle rozpisu, který zatím není oznámený. Speciální pozadí jen během eventu."]),
     dict(h="Field Research", list=["Eventové úkoly s Rare Candy jako odměnou."]),
     dict(h="GO Pass", list=["Deluxe 4,99 USD (s +6 ranky 6,99 USD): Elite Charged TM, Rare Candy XL a další. Odměny vyzvedni do st 16. 12. 20:00."]),
   ], src="https://www.dittobase.com/pokemon-go/events/pokemon-champions-celebration-event-2026")

ev(id="mega-gengar", bosses=[["raid","mega","gengar_mega"]], cat="raid", title="Mega Gengar v Mega raidech", start="2026-12-09T06:00", end="2026-12-15T22:00",
   summary="Mega Gengar v Mega raidech.", sections=[dict(h="Boss", mons=[["Mega Gengar", 0]])],
   src="https://leekduck.com/events/mega-gengar-in-mega-raids-december-2026/")

ev(id="spotlight-starly", cat="spotlight", title="Spotlight Hour: Starly", start="2026-12-10T18:00", end="2026-12-10T19:00",
   summary="Starly ve velkém, bonus 2× Catch Stardust.", sections=[dict(h="Pokémon", mons=[["Starly", 0]], note="Bonus: 2× Catch Stardust.")],
   src="https://leekduck.com/events/pokemonspotlighthour2026-12-10/")

ev(id="minior-geminids", cat="event", title="Minior Showers: Geminids", start="2026-12-11T17:00", end="2026-12-16T23:59",
   summary="Meteorický roj s Miniorem, debutují dvě nové formy Minior.",
   sections=[dict(h="Co víme", list=["Dvě nové formy Minior. Další bonusy zatím nemáme ověřené."])],
   src="https://leekduck.com/events/minior-showers-geminids-2026/")

ev(id="december-cd", cat="cd", title="Prosincový Community Day", start="2026-12-12T14:00", end="2026-12-13T17:00", featured=1,
   summary="Dva dny s Pokémony ze všech letošních Community Days, 14–17 v sobotu i v neděli.",
   sections=[
     dict(h="Featured Pokémoni", mons=[["Vulpix", 0], ["Vulpix (Alolan)", 0], ["Grookey", 0], ["Scorbunny", 0], ["Lechonk", 0], ["Tinkatink", 0], ["Piplup", 0],
       ["Zorua", 0], ["Pawniard", 0], ["Sobble", 0], ["Nickit", 0], ["Frigibax", 0], ["Gible", 0], ["Deino", 0]],
       note="Rozdělení po dnech a exkluzivní útoky zatím nemáme ověřené."),
     dict(h="Bonusy 14–17", list=["Víc featured Pokémonů ve volné přírodě", "2× XP a 2× Stardust za chycení", "2× Catch Candy",
       "2× šance na Candy XL za chycení (od levelu 31)", "1/2 vzdálenost u vajíček vložených během eventu"]),
     dict(h="Bonusy so 9:00 – ne 21:00", list=["Incense na 3 hodiny (kromě Daily Adventure)", "Lure Module na 1 hodinu", "Až 2 Special Trades za den",
       "Trade o 50 % levněji"]),
   ], src="https://leekduck.com/events/december-communityday2026/")

ev(id="ho-oh-dec", bosses=[["raid","5","ho_oh"]], cat="raid", title="5★ raidy: Ho-Oh", start="2026-12-16T06:00", end="2026-12-22T22:00",
   summary="Ho-Oh v 5★ raidech, Raid Hour st 16. 12. 18–19.",
   sections=[dict(h="Boss", mons=[["Ho-Oh", 0]]), dict(h="Raid Hour", list=["Středa 16. 12. 18:00–19:00"])],
   src="https://leekduck.com/events/ho-oh-in-5-star-raid-battles-december-2026/")

ev(id="mega-skarmory", bosses=[["raid","mega","skarmory_mega"]], cat="raid", title="Mega Skarmory v Mega raidech", start="2026-12-16T06:00", end="2026-12-22T22:00",
   summary="Mega Skarmory v Mega raidech.", sections=[dict(h="Boss", mons=[["Mega Skarmory", 0]])],
   src="https://leekduck.com/events/mega-skarmory-in-mega-raids-december-2026/")

ev(id="spotlight-bergmite", cat="spotlight", title="Spotlight Hour: Bergmite", start="2026-12-17T18:00", end="2026-12-17T19:00",
   summary="Bergmite ve velkém, bonus 2× Evolution XP.", sections=[dict(h="Pokémon", mons=[["Bergmite", 0]], note="Bonus: 2× Evolution XP.")],
   src="https://leekduck.com/events/pokemonspotlighthour2026-12-17/")

# ---------------- DO BUDOUCNA (zatím jen datum) ----------------
for i, (d, t) in enumerate([("2026-12-19", "Raid Day"),
                            ("2026-12-26", "Hatch Day"), ("2027-01-02", "Community Day Classic"), ("2027-01-09", "Super Mega Raid Day"),
                            ("2027-01-16", "Community Day"), ("2027-01-23", "Max Battle Day"), ("2027-01-30", "Super Mega Raid Day"),
                            ("2027-02-06", "Community Day"), ("2027-02-13", "Raid Day")]):
    end = d + "T23:59"
    ev(id="tba-%d" % i, cat={"Max": "max", "Com": "cd", "Rai": "raid", "Sup": "raid", "Hat": "event"}[t[:3]], title=t, start=d + "T00:00", end=end, tba=1,
       summary="Datum je potvrzené, Pokémoni a bonusy zatím ne.",
       sections=[dict(h="Co víme", list=["Datum oznámil tým Pokémon GO. Featured Pokémoni, bonusy a časy zatím oznámené nejsou."])],
       src="https://pokemongo.com/news/save-the-date-s25")

CODES = [
    ["ADIDASxPOKEMON", "Boty adidas pro avatara", "do 15. 1. 2027", "adidas"],
    ["POKEMONGOxCROCSxELECTRIFYING", "Pikachu Classic Clog pro avatara", "do 31. 12. 2027", "crocs"],
    ["POKEMONGOxCROCSxENCHANTING", "Gengar Classic Clog (oficiálně ke koupi Crocs)", "do 31. 12. 2027", "crocs"],
    ["POKEMONGOxCROCSxMELODY", "Jigglypuff Classic Platform Clog (oficiálně ke koupi Crocs)", "do 31. 12. 2027", "crocs"],
    ["LEGOxPOKEMONGOxBERRIES", "5× Razz, 5× Pinap, 5× Nanab Berry, 10× Poké Ball", "konec neoznámen", ""],
]
WEEKLY = [["Úterý", "Showcase Tuesday", "Až 20 kategorií PokéStop Showcase, přihlásit můžeš až 5 Pokémonů."],
          ["Středa", "Raid Wednesday", "Rotace 5★ a Mega bossů, Raid Hour 18–19, Rare Candy XL za osobní raid."],
          ["Čtvrtek", "GO Battle Thursday", "Spotlight Hour 18–19, 10 setů GBL místo 5, až 4× Stardust za výhry."],
          ["Pátek", "Friendship Friday", "2 Special Trades, vyšší šance na Lucky Trade, trade až o 10 % levněji, 2 Candy XL (lvl 31+). Jen osobní trade."],
          ["Neděle", "Scenic Sunday", "Víc Pokémonů i na Routes, kratší vzdálenost na Buddy Candy, Mateo až 3× denně."]]

json.dump({"updated": "2026-11-27", "events": E, "codes": CODES, "weekly": WEEKLY,
           "redeem": "https://store.pokemongo.com/offer-redemption"},
          open("../docs/data/events.json", "w"), ensure_ascii=False, separators=(",", ":"))
print(len(E), "events")
