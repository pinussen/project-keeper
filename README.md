# Project Keeper

Gemensamma instruktioner som hjälper AI att planera, driva och avsluta projekt — med samma mål och historik även när du byter verktyg.

**Planen visar var vi står. Arbetsloggen visar hur vi kom dit.** Små fristående uppgifter ska kunna göras direkt utan projektadministration.

## Vad det gör

- Definierar mål, leveranser och fasta klart-kriterier.
- Delar upp arbetet i steg med beroenden, ansvar och rimliga milstolpar.
- Uppdaterar projektplanen när arbete börjar, blockeras eller blir klart.
- Kräver en kort arbetslogg i projektets repo, även för viktiga beslut, verifiering och avbrutet arbete.
- Lägger nya förbättringsidéer i senare faser om de inte blockerar den aktuella leveransen.
- Läser aktuell plan och logg vid återupptagning och lämnar en användbar överlämning.
- Avslutar fasen när kriterierna är uppfyllda.

Detta är instruktioner och mallar, inte en agentserver, schedulerare eller teknisk garanti för modellens beteende. Reglerna är skrivna på engelska för återanvändning; agenten ska svara på användarens språk.

## Börja här

1. Klona detta repo på datorn eller servern där din agent körs.
2. Koppla in rätt instruktionsfil enligt [verktygsguiden](docs/TOOLS.md). En kloning aktiverar inte reglerna automatiskt.
3. Låt agenten återanvända projektets befintliga plan och logg. Saknas de finns [mallar](templates/).

Installationen görs en gång per berörd miljö. Bevara befintliga instruktioner. Du behöver inte installera alla verktyg samtidigt.

## Innehåll

| Fil/katalog | Syfte |
| --- | --- |
| [PROJECT_KEEPER.md](PROJECT_KEEPER.md) | Den enda gemensamma regelkällan |
| [templates/](templates/) | Lätta mallar för projektplan och arbetslogg |
| [adapters/](adapters/) | Genererade instruktioner för respektive verktyg |
| [docs/TOOLS.md](docs/TOOLS.md) | Installation, uppdatering och kontroll |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Exempel på förväntat beteende |
| [PROJECT_PLAN.md](PROJECT_PLAN.md) och [WORK_LOG.md](WORK_LOG.md) | Plan och logg för utvecklingen av Project Keeper självt |

Varje annat projekts plan och logg ska ligga i det projektets repo eller befintliga planeringssystem. Det här repot är inte en central databas över alla projekt.

## Uppdatera reglerna

Redigera PROJECT_KEEPER.md och kör:

```sh
python3 scripts/build_adapters.py
python3 scripts/build_adapters.py --check
```

På Windows kan kommandot vara `py -3`. Skriptet använder endast Pythons standardbibliotek och skriver enbart adaptrarna i detta repo. Det installerar ingenting.

Efter att ändringarna sparats i Git och hämtats till andra datorer behöver lokala kopior av instruktionerna uppdateras. Dokumenterade imports eller verifierade länkar kan minska kopieringen; se verktygsguiden.

## Omfattning för första versionen

Instruktioner, mallar, genererade adaptrar och dokumentation. Automatisk installation, en gemensam projektöversikt och installation på användarens datorer ingår inte. ChatGPT-skillen `finish-phase-one` ändras inte av detta repo.
