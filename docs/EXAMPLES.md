# Förväntat beteende

Dessa är exempel och manuella kontrollfall, inte resultat från testning av alla verktyg.

| Situation | Förväntat beteende |
| --- | --- |
| ”Ändra timeout från 10 till 20 i den här konfigen.” Ingen projektkoppling. | Gör den avgränsade ändringen och relevant kontroll. Skapa inte plan/logg. |
| Samma konfigändring ingår i en pågående produktionsmigrering. | Läs projektkontext, följ dess krav och uppdatera relevant status/logg proportionerligt. Skapa inget nytt projekt. |
| Ett nytt flerledsprojekt saknar klart-kriterier. | Formulera mål, leverans, få kontrollerbara kriterier och avgränsning innan större arbete. Fråga bara om avgörande oklarheter. |
| AI börjar ett steg som stod som ej påbörjat. | Markera Pågår när arbetet börjar; vänta inte till slutrapporten. |
| Kod är ändrad men avtalad verifiering återstår. | Behåll Pågår, eller Blockerat med orsak/ägare. Skriv vad som faktiskt har kontrollerats. |
| Något måste testprintas av användaren. | Ange blockerat kriterium, vad användaren behöver göra och nästa möjliga oberoende fas-1-arbete. Hitta inte på mer modellering som ersättning. |
| Alla avtalade säljkriterier är uppfyllda, men fler skalor vore trevligt. | Säg att fasen är klar; lägg fler skalor i senare fas. |
| Ett nedladdningspaket visar sig sakna en nödvändig del. | Koppla felet till leveranskriteriet, logga evidens och åtgärda som verkligt hinder. |
| Användaren lägger uttryckligen till stöd för H0. | Uppdatera omfattning och konsekvenser synligt. Använd inte scope-regeln för att avvisa användarens beslut. |
| ”Kanske borde vi lägga till H0?” | Behandla som idé, förklara konsekvensen innan den blir ett krav. |
| Ny session i ett annat verktyg. | Läs aktuell plan, senaste logg och relevanta filer; återuppta nästa steg utan att hitta på ny plan. |
| En tidigare lösning misslyckades. | Behåll kort anteckning om försöket, utfallet och skälet till nästa vägval. |
| Ingen tidsram har diskuterats. | Planera ordning och milstolpar utan fabricerat slutdatum. |
| En AI arbetar i en gammal klon. | Läs/synka enligt projektets arbetsflöde och bevara andras ändringar; skriv inte över aktuell status. |
