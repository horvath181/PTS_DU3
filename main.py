# importujem ostatne programy a randint
import ranking
import matchSim
from random import randint

# pocitam den v roku, rok,
# temp je pomocna premenna, ktora udrzuje vsetko v chode
day = 1
temp = True
date = 2015

# rozdelenie UEFA do skupin A - I
uefaGroups = []

# vyberie kvalifikovane timy, prida Rusko,
# spusti interkontinentalne zapasy a
# vrati tuto mnozinu statov
def getResult():
    
    nextRound = []
    res = []
    
    # vyberie po jednom z kazdej skupiny UEFA
    # druheho posunie do interkontinentalnej ligy
    for x in uefaGroups:
        res.append(x[0][0])
        nextRound.append(x[1])
    
    counter = 0
    
    # vyberie 5 najlepsich z CAF
    for x in ranking.CAF:
        res.append(x[0])
        counter += 1
        if counter == 5: break
    
    counter = 0
    
    # vyberie 4 najlepsich z AFC a 
    # dalsieho prida do interkontinentalnej ligy
    for x in ranking.AFC:
        if counter == 4:
            nextRound.append(x)
            break
        res.append(x[0])
        counter += 1
    
    counter = 0
    
    # vyberie najlepsich 5 z OFC
    for x in ranking.OFC:
        res.append(x[0])
        counter += 1
        if counter == 5: break
    
    counter = 0
    
    # vyberie najlepsich 3 z CONCACAF a
    # prida jedneho do interkontinentalnej ligy
    for x in ranking.CONCACAF:
        if counter == 3:
            nextRound.append(x)
            break
        res.append(x[0])
        counter += 1
    
    counter = 0
    
    # vyberie najlepsich 4 z CONMEBOL a
    # prida jedneho do interkontinentalnej ligy
    for x in ranking.CONMEBOL:
        if counter == 4:
            nextRound.append(x)
            break
        res.append(x[0])
        counter += 1
    
    # prida Rusko medzi kvalifikovanych
    res.append("Russia")
    
    # spusti interkontinentalnu ligu
    final = matchSim.interCon(nextRound)
    
    # prida 2 najlepsich
    res.append(final[0])
    res.append(final[1])
    
    # vrati tuto mnozinu
    return res

# tahanie do skupin UEFA
def draw(arr):
    global uefaGroups
    unused = [i for i in range(52)]
    
    for i in range(9):
        uefaGroups.append([])
        for j in range(6):
            num = randint(0, (len(unused)-1))
            uefaGroups[i].append(arr[unused[num]])
            del(unused[num])
            if len(unused) == 0: break
    
    matchSim.synch(uefaGroups, [ranking.CAF, ranking.AFC, ranking.OFC, ranking.CONCACAF, ranking.CONMEBOL])

# podla datumu simuluje, co sa ma stat tento den
def simulateDay():
    global day, date, temp
    print("___________________________________________")
    
    # prvy den taha skupiny UEFA
    if day == 1 and temp == True:
        draw(ranking.UEFA)
        print("UEFA groups have been decided.")
    
    # druhy den losuje zapasy (vsetky)
    elif day == 2 and temp == True:
        print("Matches have been drawn.")
        matchSim.simulateAll()
        temp = False
    
    # od tretieho dna spusta simulaciu vylosovanych zapasov
    else:
        print("These matches have been played.")
        matchSim.simDay()
        ranking.synch(uefaGroups, ranking.UEFA)
        ranking.update(1)
        ranking.synch(uefaGroups, ranking.UEFA)
    
    # ak presiel uz rok updatuje potrebnu tabulku a informuje
    if day == 365:
        ranking.update(2)
        date += 1
        print("A year has passed.")
        print("Current date: 1.1.{:d}".format(date))
        day = 0
    
    day += 1

# uvodne slova
print("Welcome to MS 2018 qualification simulator.")
print("Today it's 1.1.2015.")
print("206 teams are trying to qualify to World Cup. (Russia is qualified)")
print("For easier beginning every team starts with only the points acquired during",
    "the last year.")
print("You can either move on to the next day or see how the teams fare.")
print("Enjoy.")

# prednastavenie vstupu na testovanie
com = "next"

# hlavny cyklus
while(True):
    
    # vzdy vypise moznosti
    print("___________________________________________")
    print("Write \'Next\' to move on to another day.")
    print("Write \'FIFA\' to see how the teams fare in FIFA World Ranking.")
    print("Write \'WCQ\' to see how the teams fare in the World Cup qualification.")
    print("Write \'Exit\' to exit this simulation. (Your progress won\'t be saved.)")
    
    # nacita vas vyber, podla toho reaguje
    com = input("What do you do?")
    
    # skonci
    if com.lower() == "exit": break
    
    # FIFA World Ranking
    elif com.lower() == "fifa": ranking.out()
    
    # World Cup Qualification
    elif com.lower() == "wcq":
        
        # pomocna premenna aby som nemal dlhe riadky
        sc = "Which continental section do you want to see? (\'UEFA\', \'CAF\', "
        sc += "\'AFC\', \'OFC\', \'CONCACAF\', \'CONMEBOL\', \'All\')"
        
        # ktory kontinent / vsetky
        com = input(sc)
        if com.lower() == "uefa":
            
            # ak este neboli vylosovane skupiny len zobrazi timy
            if day==1:
                print("UEFA Ranking:")
                ranking.outMS(ranking.UEFA)
            
            else:
                sc = "How much info do you want? (group info: \'A\', "
                sc += "\'B\', ..., \'I\' or \'All\')"
                
                # vyber si skupinu, alebo zobraz vsetko
                com = input(sc)
                
                if com.lower() == "all":
                    print("UEFA Ranking:")
                    ranking.outMS(ranking.UEFA)
                
                elif com.lower() == "a":
                    print("UEFA Group A:")
                    print(uefaGroups[0])
                    ranking.outMS(uefaGroups[0])
                
                elif com.lower() == "b":
                    print("UEFA Group B:")
                    ranking.outMS(uefaGroups[1])
                
                elif com.lower() == "c":
                    print("UEFA Group C:")
                    ranking.outMS(uefaGroups[2])
                
                elif com.lower() == "d":
                    print("UEFA Group D:")
                    ranking.outMS(uefaGroups[3])
                
                elif com.lower() == "e":
                    print("UEFA Group E:")
                    ranking.outMS(uefaGroups[4])
                
                elif com.lower() == "f":
                    print("UEFA Group F:")
                    ranking.outMS(uefaGroups[5])
                
                elif com.lower() == "g":
                    print("UEFA Group G:")
                    ranking.outMS(uefaGroups[6])
                
                elif com.lower() == "h":
                    print("UEFA Group H:")
                    ranking.outMS(uefaGroups[7])
                
                elif com.lower() == "i":
                    print("UEFA Group I:")
                    ranking.outMS(uefaGroups[8])
                
                else:
                    print("I don't know that group.")
                
        elif com.lower() == "caf":
            print("CAF Ranking:")
            ranking.outMS(ranking.CAF)
        
        elif com.lower() == "afc":
            print("AFC Ranking:")
            ranking.outMS(ranking.AFC)
        
        elif com.lower() == "ofc":
            print("OFC Ranking:")
            ranking.outMS(ranking.OFC)
        
        elif com.lower() == "concacaf":
            print("CONCACAF Ranking:")
            ranking.outMS(ranking.CONCACAF)
        
        elif com.lower() == "conmebol":
            print("CONMEBOL Ranking:")
            ranking.outMS(ranking.CONMEBOL)
        
        elif com.lower() == "all":
            print("UEFA Ranking:")
            ranking.outMS(ranking.UEFA)
            print()
            
            print("CAF Ranking:")
            ranking.outMS(ranking.CAF)
            print()
            
            print("AFC Ranking:")
            ranking.outMS(ranking.AFC)
            print()
            
            print("OFC Ranking:")
            ranking.outMS(ranking.OFC)
            print()
            
            print("CONCACAF Ranking:")
            ranking.outMS(ranking.CONCACAF)
            print()
            
            print("CONMEBOL Ranking:")
            ranking.outMS(ranking.CONMEBOL)
        
        # zle zadany vstup pre kontinent
        else: print("I don't know that continental section.")
        
    # dalsi den
    elif com.lower() == "next":
        simulateDay()
    
    # zle zadany vstup
    else: print("That\'s not one of the options provided, please pick one of the",
                "options.")
    
    # ak sa uz dohrali vsetky zapasy
    if len(matchSim.arrMatches) == 0 and temp == False:
        
        # poviem to
        print("This is the end of this simulation.")
        
        # ziskam vysledky (spusti interkontinentalnu ligu)
        # co zobrazi vysledky este par zapasov
        arr = getResult()
        
        # vypisem, kto vsetko sa kvalifikoval
        print("___________________________________________")
        print("Teams that are qualified for World Cup in Russia are:")
        
        for x in arr:
            print(x)
        
        # ukoncim hlavny cyklus
        break
