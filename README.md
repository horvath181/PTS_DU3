# PTS---DU3
Domaca uloha 3 z Principov tvorby softveru - Simulator kvalifikacie na MS 2018 vo futbale

Zadanie:

Domácu úlohu odovzdajte ako GITovský repozitár e-mailom na relatko@gmail.com. Do subjectu napiste PTS DU2. Nezabudnite napisat svoje meno. Termín na odovzdanie úlohy je 27.4.2017 23:00

Úlohou je navrhnúť systém, ktorý simuluje proces kvalifikácie na a samotné majstrovstvá sveta vo futbale 2018. Svoj dizajn popíšte. Urobte čiastočnú implemntáciu, ktorá bude simulovať niejaký iný, vymyslený, zjednodušený turnaj. Implementácia nemusí (a ani to neočakavam) byť postačujúca na simuláciu klalifikácie a MS, avšak dizajn má byť dostatočne flexibilný aby implementácia ostatných featurov nebola zásadným problémom vyžadujúcim kompletnú zmenu designu. 
Systém sa nainicializuje do stavu zodpovedajúcemu 1.1.2015. Systém spolupracuje s dvoma inými podsystémami: FIFA World Ranking a Simulátor zápasov (týmito systémami sa nemáte zaoberať, máte však definovať ich interface a na čiastkovú impleméntáciu budete potrebovať ich stuby - triviálne nakódené verzie). 

Systém má dva use casy.
Posunuť sa o deň vpred
Systém odsimuluje (s pomocou simulátora zápasov a FIFA World Ranking) možný vývoj počas nasledujúceho jedného dňa a vytvorí nový stav turnaja. Táto simulácia zahŕňa: zaznamenanie výsledkov zápasov, zmenu tabuliek, žrebovanie tímov do jednotlivých skupín (nasadzovanie do žrebovania určuje FIFA World Ranking), postup tímov medzi rôznymi časťami súťaže.
Zistiť aktuálny stav turnaja
Systém vie poskytnúť klientovy aktualny stav sútaže (výsledky historických zápasov, aktuálne tabuľky, tabuľky už ukončených častí turnaja).
Pre všeobecný prehľad ako prebieha kvalifikácia na MS vo futbale si pozrite Wikipediu. Pre čo najrýchlejšie pochopenie potenciálnej zlošitosti kvalifikačného procesu odporúčam si pozrieť si ako to prebieha v Ázii. 

Ak vám niečo v zadaní chýba, alebo sa vám niečo veľmi nepáči, kľudom si ho obmeňte.

Moj pristup:

Celý program využíva 4 súbory:
* main.py - hlavný kód
* matchSim.py - kód, ktorý zabezpečuje simuláciu zápasov a jednotlivých dní (mal byť podľa zadania iba stub, nesplnil som)
* ranking.py - kód, ktorý udržiava stav tabuliek a vypisuje ho (mal byť podľa zadania iba stub, nesplnil som)
* ranking.csv - súbor obsahujúci počet počiatočných bodov a kontinent pre každý tím

main.py:

Hlavný program. Popisuje, čo treba robiť aby sa účastník simulácie dostal ďalej. Účastník simulácie sa vie posunúť o deň vpred, pozrieť na tabuľky tímov (zjednodušený FIFA World Ranking, tabuľky kontinentov) alebo ukončiť svoju činnosť (postup sa neukladá). Až prebehnú všetky zápasy vyberie kvalifikované tímy (aj Rusko) a spustí interkontinentálne zápasy. Nakoniec vypíše kvalifikované tímy. Obsahuje zopár vecí, ktoré som mohol (a asi aj mal) robiť inde, ale už nemám čas ani vôľu to prepisovať (napríklad rozlosovanie do skupín UEFA).


matchSim.py:

Tento program sa stará o simulovanie jednotlivých zápasov. Používa na to list, do ktorého na začiatku vložím všetky zápasy a potom náhodne vyberám 6 zápasov denne. Samotná simulácia funguje nasledovne:
* zoberiem si náhodné číslo z intervalu 0 - 210
* 8-krát testujem, či padne gól (8 sa mi zdalo ako prijateľné množstvo). To záleží na tom, či je číslo z dolnej časti intervalu (gól dali hostia), zo strednej časti intervalu (gól dali domáci) alebo je vyššie (nikto nedal gól).
* následne funkcia vráti počty gólov
* z toho sa vonkajšia funkcia rozhodne, kto vyhral, vypíše výsledok a zapíše do príslušných tabuliek

Vo všetkých skupinách (UEFA A - I, AFC, CAF, OFC, CONCACAF, CONMEBOL) hrá každý s každým. Po ukončení všetkých zápasov sa z každej skupiny vyberú 3, 4 alebo 5 najlepší (okrem UEFA, tam je z každej skupiny 1) a z ostatných sa posunú tími do interkontinentálnych zápasov. Tie sa odohrajú automaticky ešte ten deň, keď sa dohrá posledný zápas. Každý tím dostane jeden zápas proti náhodnému protivníkovi. Následne podľa počtu bodov, rozdielu strelených a získaných gólov a poradia v tabuľke FIFA World Ranking sa vyberú ďalší dvaja, ktorí tiež postupujú.


ranking.py:

Tento program na začiatku načíta počet bodov každého tímu a vytvorí lokálne tabuľky. Taktiež zabezpečuje výpis týchto tabuliek a ich usporiadanie. Pre FIFA World Ranking pripočítava získané body formou:

Body = V (počet bodov za výhru) * S (sila súpera podľa)
* V: Tím získa 3 body za výhru, 1 za remízu, 0 za prehru.
* S: S = 206-(umiestnenie súpera v tabuľke)

Body z predošlých 3 rokov si pamätám, s tým, že majú postupne váhu:
* Tento rok: 100%
* Minulý rok: 50%
* Predminulý rok: 30%
* Tri roky dozadu: 20%

Ostatné tabuľky začínajú na nule, predusporiadané podľa FIFA World Ranking. Tieto tabuľky sa usporiaduvajú podľa počtu získaných bodov a následne podľa gólov.


ranking.csv:

Obsahuje informácie o tímoch:
* názov tímu
* kontinent, na ktorom sa nachádza
* počet bodov získaných za rok 2014 (obsahuje aj priestor na body získané v ostatných štyroch rokoch, no nemal som čas nájsť ich)
