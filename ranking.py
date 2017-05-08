# csv na pracu so suborom, operator na usporaduvanie
import csv
import operator

# FIFA World Ranking
sortedRanking = []

# Vsetky staty v UEFA, CAF, AFC, OFC, CONCACAF, CONMEBOL
UEFA = []
CAF = []
AFC = []
OFC = []
CONCACAF = []
CONMEBOL = []

# nacita a vytvori zakladne tabulky z ranking.csv
def load():
    
    global sortedRanking
    
    with open('ranking.csv', newline='') as csvfile:
	    ranking = csv.reader(csvfile, delimiter=',')
	    ranking = [[continent, state,
	    float(float(points0) + float(points1) * 0.5 +
	    float(points2) * 0.3 + float(points3) * 0.2),
	    float(points0), float(points1), float(points2), float(points3)]
	    for state, continent, points0, points1, points2, points3 in ranking]
	    
	    sortedRanking = sorted(ranking, key=operator.itemgetter(2), reverse=True)
	
    counter = 0
    
    for x in sortedRanking:
        x.append(counter)
        counter += 1
        
    update(0)

# Vypise FIFA World Ranking
def out():
    
    sortedRanking.sort(key=operator.itemgetter(2), reverse = True)
    print("FIFA World Ranking:")
    print("Rank {:<30s}{:>30s}".format("State","Points"))
    counter = 1
    
    for x in sortedRanking:
        s = str(counter) + '.' 
        print("{:>4s} {:<30s}{:>30.0f}".format(s, x[1], x[2]))
        counter += 1

# Vypise tabulku arr vo formate MS
def outMS(arr):
    
    print("Rank {:<30s} {:>30s} {:s} {:s}   {:s}".format("State","Win","Draw","Lose",
        "Points"))
    counter = 1
    
    for x in arr:
        s = str(counter) + '.' 
        points = 3*x[1] + x[2]
        print("{:>4s} {:<30s}{:>30.0f} {:>4.0f} {:>4.0f} {:>6.0f}".format(s, x[0],
            x[1], x[2], x[3], points))
        counter += 1

#synchronizuje tabulku uefaGroups z mainu s tabulkou UEFA
def synch(outArr, arr):
    
    for x in outArr:
        for y in x:
            for i in range(len(arr)-1):
                if y[0]==arr[i][0]:
                    arr[i][1] = y[1]
                    arr[i][2] = y[2]
                    arr[i][3] = y[3]
                    arr[i][4] = y[4]
                    arr[i][5] = y[5]
                    y[6] = arr[i][6]

# updatuje tabulky, t.j. usporiada podla prislusnych parametrov
def update(temp):
    
    global sortedRanking, UEFA, CAF, AFC, OFC, CONCACAF, CONMEBOL
    
    # uvodne nacitanie globalnych tabuliek
    if temp == 0:
        for x in sortedRanking:
            rank = x[7]
            if x[0] == "UEFA":
                # kazda tabulka ma nazov statu (state),
                # pocet vyhier (W), pocet remiz (D),
                # pocet prehier (L), body (P = 3*W + D),
                # rozdiel golov (G) a rank vo FIFA World Ranking
                #           state, W, D, L, P, G, rank
                UEFA.append([x[1], 0, 0, 0, 0, 0, rank])
                
            elif x[0] == "CAF":
                CAF.append([x[1], 0, 0, 0, 0, 0, rank])
                
            elif x[0] == "AFC":
                AFC.append([x[1], 0, 0, 0, 0, 0, rank])
                
            elif x[0] == "OFC":
                OFC.append([x[1], 0, 0, 0, 0, 0, rank])
                
            elif x[0] == "CONCACAF":
                CONCACAF.append([x[1], 0, 0, 0, 0, 0, rank])
                
            elif x[0] == "CONMEBOL":
                CONMEBOL.append([x[1], 0, 0, 0, 0, 0, rank])
                
            rank += 1
            
    # bezny update
    elif temp == 1:
        sortedRanking.sort(key = operator.itemgetter(2), reverse=True)
        check(UEFA)
        check(CAF)
        check(AFC)
        check(OFC)
        check(CONCACAF)
        check(CONMEBOL)
        
    # update po roku
    elif temp == 2:
        for x in sortedRanking:
            x[6] = x[5]
            x[5] = x[4]
            x[4] = x[3]
            x[3] = 0.00
            x[2] = 0.5*x[4] + 0.3*x[5] + 0.2*x[6]

# update kazdej z tabuliek
def check(arr):
    
    arr.sort(key = operator.itemgetter(4, 5), reverse = True)
    
    for x in sortedRanking:
        for y in arr:
            if x[1] == y[0]:
                y[6] = x[7]


# automaticke nacitanie
load()
