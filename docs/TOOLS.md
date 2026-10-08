# Användning i olika verktyg

Kontrollerat mot officiell dokumentation 2026-10-08. Verktygsversion, agenttyp och vald miljö kan påverka hur instruktioner laddas. De här anvisningarna installerar inget automatiskt.

## Gemensam princip

PROJECT_KEEPER.md är regelkällan. Adaptrarna innehåller samma text med verktygsspecifik frontmatter där den behövs. Generera dem med scripts/build_adapters.py; redigera inte kopiorna separat.

Läs befintliga instruktioner innan installation. Använd en separat fil när det stöds; annars infoga ett avgränsat Project Keeper-avsnitt utan att ersätta befintligt innehåll. Vid uppdatering ersätt endast det avsnittet och undvik dubletter. Byt inte ut en befintlig AGENTS.md eller CLAUDE.md mot en länk som skulle dölja dess andra instruktioner.

Installerade regler ska finnas där agenten faktiskt körs. Lokal Windows, WSL, SSH, container och server kan vara olika miljöer med egna hemkataloger. Ett separat klonat repo laddas inte automatiskt bara för att det finns på disken.

## Platser

| Verktyg | Adapter | Placering / aktivering |
| --- | --- | --- |
| Kiro IDE/CLI | adapters/kiro/project-keeper.md | Separat fil i ~/.kiro/steering/ för alla lokala projekt, eller .kiro/steering/ i ett projekt. inclusion: always anges i filen. |
| Codex CLI | adapters/codex/AGENTS.md | Infoga i aktiv global instruktionsfil under CODEX_HOME, normalt ~/.codex/AGENTS.md. Om AGENTS.override.md finns väljs den i stället. Projektets egna instruktioner kan påverka slutresultatet. |
| Claude Code CLI och Claude Code-extensionen i VS Code | adapters/claude/CLAUDE.md | Infoga i ~/.claude/CLAUDE.md, eller använd en dokumenterad @path-import till den klonade PROJECT_KEEPER.md. Använd den verkliga lokala sökvägen. |
| Copilot Agent Host i VS Code | adapters/copilot/copilot-instructions.md | Infoga i ~/.copilot/copilot-instructions.md för personliga instruktioner. |
| Copilot Local i VS Code | adapters/copilot/project-keeper.instructions.md | Skapa en användarinstruktion via Chat: Open Customizations för vald agent och använd adapterns innehåll. applyTo: "**" täcker matchande filarbete. |
| Copilot projektinstruktioner | adapters/copilot/copilot-instructions.md | Infoga i projektets .github/copilot-instructions.md, även för projektchatt där en filmatchad instruktion inte nödvändigtvis aktiveras. |
| OpenClaw | adapters/openclaw/AGENTS.md | Infoga i AGENTS.md i varje berörd agents verkliga workspace. Standardworkspace är ofta ~/.openclaw/workspace, men kontrollera aktuell konfiguration. |

Kiro custom agents behöver uttryckligen inkludera relevanta steering-filer i sina resources. Anta inte att global steering automatiskt följer med varje custom agent.

”Claude i VS Code” kan betyda två saker: Claude-modellen vald i Copilot använder Copilots instruktioner; Claude Code-extensionen använder Claude Codes instruktioner.

Copilots instruktioner gäller agent/chat, inte inline-komplettering medan du skriver. För Copilot Local är en användarinstruktion med filmatchning inte en garanti för att ren planeringschatt alltid får den; använd projektinstruktionen eller bifoga instruktionen där det behövs. Välj rätt agenttyp i VS Codes inställningar för instruktioner.

OpenClaw ska återanvända befintlig ärendehantering för planen när sådan finns. Arbetsloggen ska fortfarande finnas i projektets repo och länka relevant ärende. En workspace-instruktion ersätter inte projektets faktiska status.

## Import, länk eller kopia

Claude Code har dokumenterad @path-import i CLAUDE.md. Den syntaxen ska inte antas fungera i andra appar. För en fristående instruktionsfil kan en symbolisk länk vara praktisk om den aktuella miljön stöder och faktiskt läser den; kontrollera detta lokalt. En vanlig kopia är enklare men måste uppdateras efter git pull. Automatiserad installation/synkning ingår inte i första versionen.

## Installationsprompt till en lokal agent

> Läs Project Keepers README.md, PROJECT_KEEPER.md och docs/TOOLS.md. Installera reglerna för det verktyg och den miljö vi arbetar i. Identifiera först den faktiska instruktionsplatsen och läs befintliga filer. Bevara allt orelaterat innehåll och ta backup av filer som ändras. Använd en separat fil eller dokumenterad import där det passar; annars ett tydligt avgränsat avsnitt som uppdateras utan dubletter. Ändra inte andra verktygs konfiguration om de inte ingår i min begäran. Återanvänd projektets plan och logg. Rapportera vilka filer som ändrades och vad som behöver kontrolleras i en ny session. Påstå inte att reglerna laddats enbart för att en fil skapats.

## Kontrollera aktivering

Öppna en ny session och kontrollera instruktionslistan/referenserna där verktyget erbjuder det. Kontrollera faktiska sökvägar och eventuella overrides om instruktionen saknas. Prova relevanta beteendeexempel i EXAMPLES.md. Ett korrekt enstaka svar är inte bevis för att alla framtida svar följer reglerna.

Håll samma aktuella projektplan tillgänglig när du byter verktyg. För flera kloner krävs vanlig versionshantering eller en gemensam läsbar ärendekälla; osynkade statuskopior ger ingen kontinuitet.

## Officiella källor

- Kiro: https://kiro.dev/docs/steering/
- Codex: https://developers.openai.com/codex/guides/agents-md
- Claude Code: https://code.claude.com/docs/en/memory
- VS Code: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- OpenClaw: https://docs.openclaw.ai/concepts/agent-workspace
