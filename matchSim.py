# operator na usporiadania
import operator
# sortedRanking na pridanie bodov do FIFA World Ranking
from ranking import sortedRanking
# randint na randomizaciu
from random import randint

#tabulky jednotlivych skupin
arr1A = []
arr1B = []
arr1C = []
arr1D = []
arr1E = []
arr1F = []
arr1G = []
arr1H = []
arr1I = []
arrCaf = []
arrAfc = []
arrOfc = []
arrConc = []
arrConm = []
# tabulka planovanych zapasov
arrMatches = []

# simuluje zapas medzi timami podla ich umiestnenia a vrati pocty golov
def sim(rankA, rankB):
    goalA = 0
    goalB = 0
    lower = 70 - abs(rankA - rankB)
    higher = 140 - abs(rankA - rankB)
    num = randint(0, 210)
    for i in range(8):
        if num in range(lower):
            if rankA>rankB: goalA += 1
            else: goalB += 1
        elif num in range(lower, higher):
            if rankA<rankB: goalA += 1
            else: goalB += 1
        num = randint(0, 210)
    return [goalA, goalB]

# krkolomny sposob, ako si preniest tabulky z inej casti programu
def synch(arr1, arr2):
    global arr1A, arr1B, arr1C, arr1D, arr1E
    global arr1F, arr1G, arr1H, arr1I
    global arrCaf, arrAfc, arrOfc, arrConc, arrConm
    arr1A = arr1[0]
    arr1B = arr1[1]
    arr1C = arr1[2]
    arr1D = arr1[3]
    arr1E = arr1[4]
    arr1F = arr1[5]
    arr1G = arr1[6]
    arr1H = arr1[7]
    arr1I = arr1[8]
    arrCaf = arr2[0]
    arrAfc = arr2[1]
    arrOfc = arr2[2]
    arrConc = arr2[3]
    arrConm = arr2[4]

# vonkajsia funkcia simulacie tahania zapasov
def simulateAll():
    global arr1A, arr1B, arr1C, arr1D, arr1E
    global arr1F, arr1G, arr1H, arr1I
    global arrCaf, arrAfc, arrOfc, arrConc, arrConm
    simulate(arr1A, len(arr1A))
    simulate(arr1B, len(arr1B))
    simulate(arr1C, len(arr1C))
    simulate(arr1D, len(arr1D))
    simulate(arr1E, len(arr1E))
    simulate(arr1F, len(arr1F))
    simulate(arr1G, len(arr1G))
    simulate(arr1H, len(arr1H))
    simulate(arr1I, len(arr1I))
    simulate(arrCaf, len(arrCaf))
    simulate(arrAfc, len(arrAfc))
    simulate(arrOfc, len(arrOfc))
    simulate(arrConc, len(arrConc))
    simulate(arrConm, len(arrConm))

# funkcia vytvori vsetky kombinacie zapasov a vlozi ich do tabulky planovanych zapasov
def simulate(arr, ran):
    for current in range(ran-1):
        for i in range(current+1, ran):
            arrMatches.append([arr, arr[current][0], arr[i][0]])
            arrMatches.append([arr, arr[i][0], arr[current][0]])

# pomocna funkcia na najdenie pozicie statu v liste
def find(state, arr, tmp = 1):
    if tmp == 2:
        pos1 = 1
        pos2 = 2
        ret = []
        for i in range(len(arr)):
            if arr[i][pos1] == state or arr[i][pos2] == state:
                ret.append(i)
        return ret
    else:
        pos = 0
        if tmp == 0:
            pos = 1
        for i in range(len(arr)):
            if arr[i][pos] == state:
                return i

# simulator jedneho dna
def simDay():
    global arrMatches
    # ak mame uz len 6 alebo menej zapasov vyberie vsetky
    if len(arrMatches)<=6:
        while len(arrMatches)>0:
            # odsimuluje po jednom
            simMatch(arrMatches[0][0], arrMatches[0][1], arrMatches[0][2])
            # upravi pocet bodov
            for x in arrMatches[0][0]:
                x[4] = 3*x[1] + x[2]
            # usporiada danu tabulku
            arrMatches[0][0].sort(key=operator.itemgetter(4, 5), reverse=True)
            # vymaze tento zapas z tabulky
            del(arrMatches[0])
    # inak vyberie 6 nahodnych zapasov
    # a kona rovnako
    else:
        pos = int(len(arrMatches)/6)
        pos1 = 0
        pos2 = pos
        num1 = randint(pos1, pos2)
        pos1 = pos
        pos2 = pos*2
        num2 = randint(pos1, pos2)
        pos1 = pos*2
        pos2 = pos*3
        num3 = randint(pos1, pos2)
        pos1 = pos*3
        pos2 = pos*4
        num4 = randint(pos1, pos2)
        pos1 = pos*4
        pos2 = pos*5
        num5 = randint(pos1, pos2)
        pos1 = pos*5
        pos2 = len(arrMatches)-1
        num6 = randint(pos1, pos2)
        simMatch(arrMatches[num1][0], arrMatches[num1][1], arrMatches[num1][2])
        simMatch(arrMatches[num2][0], arrMatches[num2][1], arrMatches[num2][2])
        simMatch(arrMatches[num3][0], arrMatches[num3][1], arrMatches[num3][2])
        simMatch(arrMatches[num4][0], arrMatches[num4][1], arrMatches[num4][2])
        simMatch(arrMatches[num5][0], arrMatches[num5][1], arrMatches[num5][2])
        simMatch(arrMatches[num6][0], arrMatches[num6][1], arrMatches[num6][2])
        for x in arrMatches[num1][0]:
            x[4] = 3*x[1] + x[2]
        for x in arrMatches[num2][0]:
            x[4] = 3*x[1] + x[2]
        for x in arrMatches[num3][0]:
            x[4] = 3*x[1] + x[2]
        for x in arrMatches[num4][0]:
            x[4] = 3*x[1] + x[2]
        for x in arrMatches[num5][0]:
            x[4] = 3*x[1] + x[2]
        for x in arrMatches[num6][0]:
            x[4] = 3*x[1] + x[2]
        arrMatches[num1][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        arrMatches[num2][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        arrMatches[num3][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        arrMatches[num4][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        arrMatches[num5][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        arrMatches[num6][0].sort(key=operator.itemgetter(4, 5), reverse=True)
        del(arrMatches[num6], arrMatches[num5], arrMatches[num4], arrMatches[num3], arrMatches[num2], arrMatches[num1])

# simuluje zapas podla tabulky, v ktorej je a nazvov statov
# nasledne upravi FIFA World Ranking a prislusnu tabulku
def simMatch(arr, home, away):
    global sortedRanking
    homeIndex = find(home, arr)
    awayIndex = find(away, arr)
    homeF = find(home, sortedRanking, 0)
    awayF = find(away, sortedRanking, 0)
    goals = sim(arr[homeIndex][6], arr[awayIndex][6])
    print("{:<15s} {:>15d}:{:<15d} {:>15s}".format(home, goals[0], goals[1], away))
    if goals[0]>goals[1]:
        arr[homeIndex][1] += 1
        arr[awayIndex][3] += 1
        arr[homeIndex][5] += goals[0]-goals[1]
        arr[awayIndex][5] -= goals[0]-goals[1]
        sortedRanking[homeF][3] += float(3*(206 - arr[awayIndex][6]))
        return 1
    elif goals[0] == goals[1]:
        arr[homeIndex][2] += 1
        arr[awayIndex][2] += 1
        sortedRanking[homeF][3] += float(206 - arr[awayIndex][6])
        sortedRanking[awayF][3] += float(206 - arr[homeIndex][6])
        return 0
    else:
        arr[homeIndex][3] += 1
        arr[awayIndex][1] += 1
        arr[homeIndex][5] -= goals[1]-goals[0]
        arr[awayIndex][5] += goals[1]-goals[0]
        sortedRanking[awayF][3] += float(3*(206 - arr[homeIndex][6]))
        return 2

# simulator interkontinentalnych zapasov
def interCon(arr):
    # najprv vylosuje, kto pojde proti komu
    simulate(arr, len(arr))
    print("Inter-confederation matches:")
    # pripravy prazdnu tabulku (vynuluje skore)
    for x in arr:
        x[1] = 0
        x[2] = 0
        x[3] = 0
        x[4] = 0
        x[5] = 0
    # kazdy odohra 1 zapas, preto mam pole este nevytiahnutych
    unused = [x[0] for x in arr]
    while len(unused) > 0:
        # nahodne vyberiem zapas
        num = randint(0, len(arrMatches)-1)
        state1 = arrMatches[num][1]
        state2 = arrMatches[num][2]
        # overim, ze tieto timy este nehrali
        if state1 in unused and state2 in unused:
            simMatch(arrMatches[num][0], arrMatches[num][1], arrMatches[num][2])
            # odstranim prislusne staty z unused
            del(unused[unused.index(state1)])
            del(unused[unused.index(state2)])
    # prepocitam skore
    for x in arr:
        x[4] = 3*x[1] + x[2]
    # usporiadam tabulku
    arr = sorted(sorted(arr, key=operator.itemgetter(6)), key=operator.itemgetter(4,5), reverse=True)
    # vyberiem 2 najlepsich
    return [arr[0][0], arr[1][0]]