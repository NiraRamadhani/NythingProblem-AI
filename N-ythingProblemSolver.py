import random
import math
import copy
import numpy as np

def ReadFile(fileName) :
    #input: nama file
    #output: isi file dalam bentuk list of tuple
    unitList = []
    file = open(fileName, "r")
    for line in file :
        detail = []
        for word in line.split() :
            detail.append(word)
        tuple(detail)
        unitList.append(detail)
    return unitList

def AvailCheck(x, y, tempList) :
    #input: koordinat x,y petak yang ingin diperiksa; list bidak yang ada
    #output: True jika petak kosong, False jika petak sudah terisi bidak
    for detail in tempList :
        if detail[2] == x and detail[3] == y :
            return False
    return True

def GeneratePos(unitList) :
    #input: list of tuple hasil bacaan file
    #output: list of tuple(WARNA, JENIS, posisi x, posisi y)
    unitDetail = []
    for info in unitList :
        for i in range(int(info[2])) :
            elmt = (info[0],info[1])
            x = random.randint(0,7)
            y = random.randint(0,7)
            aman = True
            if unitDetail :
                aman = AvailCheck(x, y, unitDetail)
            while not aman :
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                aman = AvailCheck(x, y, unitDetail)
            pos = (x, y)
            elmt = elmt + pos
            unitDetail.append(elmt)
    return unitDetail

def KnightAtkCount(colour, i, j, tempList) :
    #input: warna knight, posisi (x,y) knight, list bidak
    #output: tuple(jumlah serang knight ini ke warna sama, jumlah serang knight ini ke warna beda)
    sCount = 0; #counter warna sama
    dCount = 0; #counter warna beda
    if i+2 <= 7 and j-1 >= 0 :
        if not AvailCheck(i+2, j-1, tempList) :
            for elmt in tempList :
                if elmt[2] == i+2 and elmt[3] == j-1 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i+2 <= 7 and j+1 <= 7 :
        if not AvailCheck(i+2, j+1, tempList) :
            for elmt in tempList :
                if elmt[2] == i+2 and elmt[3] == j+1 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i-2 >= 0 and j-1 >= 0 :
        if not AvailCheck(i-2, j-1, tempList) :
            for elmt in tempList :
                if elmt[2] == i-2 and elmt[3] == j-1 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i-2 >= 0 and j+1 <= 7 :
        if not AvailCheck(i-2, j+1, tempList) :
            for elmt in tempList :
                if elmt[2] == i-2 and elmt[3] == j+1 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i+1 <= 7 and j-2 >= 0 :
        if not AvailCheck(i+1, j-2, tempList) :
            for elmt in tempList :
                if elmt[2] == i+1 and elmt[3] == j-2 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i+1 <= 7 and j+2 <= 7 :
        if not AvailCheck(i+1, j+2, tempList) :
            for elmt in tempList :
                if elmt[2] == i+1 and elmt[3] == j+2 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i-1 >= 0 and j-2 >= 0 :
        if not AvailCheck(i-1, j-2, tempList) :
            for elmt in tempList :
                if elmt[2] == i-1 and elmt[3] == j-2 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    if i-1 >= 0 and j+2 <= 7 :
        if not AvailCheck(i-1, j+2, tempList) :
            for elmt in tempList :
                if elmt[2] == i-1 and elmt[3] == j+2 :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
    return (sCount, dCount)

def RookAtkCount(colour, i, j, tempList) :
    #input: warna Rook, posisi (x,y) rook, list bidak
    #output: tuple(jumlah serang rook ini ke warna sama, jumlah serang rook ini ke warna beda)
    sCount = 0
    dCount = 0
    for x in range(i+1, 8) :
        if not AvailCheck(x, j, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == j :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
    for x in range(i-1, -1, -1) :
        if not AvailCheck(x, j, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == j :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
    for y in range(j+1, 8) :
        if not AvailCheck(i, y, tempList) :
            for elmt in tempList :
                if elmt[2] == i and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
    for y in range(j-1, -1, -1) :
        if not AvailCheck(i, y, tempList) :
            for elmt in tempList :
                if elmt[2] == i and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
    return (sCount, dCount)

def BishopAtkCount(colour, i, j, tempList) :
    #input: warna Bishop, posisi (x,y) bishop, list bidak
    #output: tuple(jumlah serang bishop ini ke warna sama, jumlah serang bishop ini ke warna beda)
    sCount = 0
    dCount = 0
    x = i+1
    y = j-1
    while (x <= 7 and y >= 0) :
        if not AvailCheck(x, y, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
        x = x + 1
        y = y - 1
    x = i+1
    y = j+1
    while (x <= 7 and y <= 7) :
        if not AvailCheck(x, y, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
        x = x + 1
        y = y + 1
    x = i-1
    y = j+1
    while (x >= 0 and y <= 7) :
        if not AvailCheck(x, y, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
        x = x - 1
        y = y + 1
    x = i-1
    y = j-1
    while (x >= 0 and y >= 0) :
        if not AvailCheck(x, y, tempList) :
            for elmt in tempList :
                if elmt[2] == x and elmt[3] == y :
                    if elmt[0] == colour :
                        sCount = sCount + 1
                    else :
                        dCount = dCount + 1
            break
        x = x - 1
        y = y - 1
    return (sCount, dCount)

def QueenAtkCount(colour, i, j, tempList) :
    #input: warna queen, posisi (x,y) queen, list bidak
    #output: tuple(jumlah serang queen ini ke warna sama, jumlah serang queen ini ke warna beda)
    temp1 = RookAtkCount(colour, i, j, tempList)
    temp2 = BishopAtkCount(colour, i, j, tempList)
    return (temp1[0]+temp2[0], temp1[1]+temp2[1])

def TotalAtkCount(tempList) :
    #input: list bidak
    #output: tuple(jumlah serang semua bidak sewarna, jumlah serang bidak berbeda warna)
    sCount = 0
    dCount = 0
    for elmt in tempList :
        if elmt[1] == "ROOK" :
            temp = RookAtkCount(elmt[0], int(elmt[2]), int(elmt[3]), tempList)
            sCount = sCount + temp[0]
            dCount = dCount + temp[1]
        elif elmt[1] == "BISHOP" :
            temp = BishopAtkCount(elmt[0], int(elmt[2]), int(elmt[3]), tempList)
            sCount = sCount + temp[0]
            dCount = dCount + temp[1]
        elif elmt[1] == "KNIGHT" :
            temp = KnightAtkCount(elmt[0], int(elmt[2]), int(elmt[3]), tempList)
            sCount = sCount + temp[0]
            dCount = dCount + temp[1]
        elif elmt[1] == "QUEEN" :
            temp = QueenAtkCount(elmt[0], int(elmt[2]), int(elmt[3]), tempList)
            sCount = sCount + temp[0]
            dCount = dCount + temp[1]
    return (sCount, dCount)

def PrintBoard(tempList) :
    #input: list bidak
    #output: print ke layar kondisi papan
    for i in range(8) :
        line = ""
        for j in range(8) :
            if AvailCheck(i, j, tempList) :
                line = line + "-"
            else :
                for elmt in tempList :
                    if elmt[2] == i and elmt[3] == j :
                        if elmt[0] == "WHITE" :
                            if elmt[1] == "QUEEN" :
                                line = line + "Q"
                            elif elmt[1] == "ROOK" :
                                line = line + "R"
                            elif elmt[1] == "KNIGHT" :
                                line = line + "K"
                            elif elmt[1] == "BISHOP" :
                                line = line + "B"
                        elif elmt[0] == "BLACK" :
                            if elmt[1] == "QUEEN" :
                                line = line + "q"
                            elif elmt[1] == "ROOK" :
                                line = line + "r"
                            elif elmt[1] == "KNIGHT" :
                                line = line + "k"
                            elif elmt[1] == "BISHOP" :
                                line = line + "b"
            line = line + " "

        print(line+str(i+1))
    print("1 2 3 4 5 6 7 8")


def hill_climbing(unitList):
    #input : hasil parsing dari file berupa list
    #output : list bidak setelah optimasi
    current = GeneratePos(unitList)
    initAtk = TotalAtkCount(current)
    PrintBoard(current)
    print(initAtk[0], initAtk[1])
    if not current :
        return False

    neighbor_list = []

    inStream = input("Jumlah iterasi saat bertemu flat : ")
    limit = int(inStream)
    count = 0
    FoundLocalMax = False
    while (not (FoundLocalMax)) and (count < limit): #asumsi maksimal 100 untuk flat
        for bidak in current:
            bidak_copy = []
            neighbor = []
            for x in range(0,8):
                for y in range(0,8):
                    listtemp = copy.copy(current)
                    if (AvailCheck(x, y, listtemp)):
                        if not ((x == bidak[2]) and (y == bidak[3])):
                            bidak_copy = (bidak[0], bidak[1], x, y)
                            listtemp.remove(bidak)
                            neighbor = copy.deepcopy(listtemp)
                            neighbor.append(bidak_copy)
                            neighbor_list.append(neighbor)

        isFirst = True
        i = 1
        for item in neighbor_list:
            itemAtk = TotalAtkCount(item)
            if isFirst:
                Max = itemAtk[1] - itemAtk[0]
                ItemMax = item
                isFirst = False
            elif ((itemAtk[1] - itemAtk[0]) > Max):
                Max = itemAtk[1] - itemAtk[0]
                ItemMax = item
            i = i + 1

        if (Max > (initAtk[1] - initAtk[0])):
            current = ItemMax
            initAtk = TotalAtkCount(current)
            neighbor_list.clear()
        elif (Max == (initAtk[1] - initAtk[0])):
            count = count + 1
            neighbor_list.clear()
        elif (Max < (initAtk[1] - initAtk[0])):
            FoundLocalMax = True
            neighbor_list.clear()

    return (current)

def simulatedAnnealing(unitList):
    #input: list hasil parsing dari file eksternal
    #output: list bidak setelah dioptimasi
    list = GeneratePos(unitList)
    atkCount = TotalAtkCount(list)
    PrintBoard(list)
    print(atkCount[0], atkCount[1])
    if not list :
        return False
    N = atkCount[1] - atkCount[0]
    i = int(input("Jumlah Step = "))
    j = i
    T = np.log(j - i + 1)
    while (i > 0) :
        bidak = random.choice(list)
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        while not (AvailCheck(x, y, list)) :
            x = random.randint(0, 7)
            y = random.randint(0, 7)
        bidakt = (bidak[0],bidak[1])+(x,y)
        listtemp = list.copy()
        listtemp.remove(bidak)
        listtemp.append(bidakt)
        atkCount = TotalAtkCount(listtemp)
        Ntemp = atkCount[1]-atkCount[0]
        if(N <= Ntemp):
            N = Ntemp
            list = []
            list = listtemp.copy()
        elif(N > Ntemp):
            prob = math.exp(-T)
            Q = math.floor(prob * 100)
            W = random.randint(1, 100)
            if W <= Q :
                N = Ntemp
                list = []
                list = listtemp.copy()
        i = i - 1
        T = np.log(j - i + 1)
    return (list)

def geneticAlgorithm(unitList):
    #input: list hasil parsing dari file eksternal
    #output: list bidak setelah dioptimasi
    fullList = []
    
    kromA = GeneratePos(unitList)
    atk = TotalAtkCount(kromA)
    PrintBoard(kromA)
    print(atk[0], atk[1])

    if not kromA :
        return False
    
    selisih = atk[1] - atk[0]
    var = (kromA, selisih)
    fullList.append(var)
    
    kromB = GeneratePos(unitList)
    atk = TotalAtkCount(kromB)
    selisih = atk[1] - atk[0]
    var = (kromB, selisih)
    fullList.append(var)
    
    kromC = GeneratePos(unitList)
    atk = TotalAtkCount(kromC)
    selisih = atk[1] - atk[0]
    var = (kromC, selisih)
    fullList.append(var)

    kromD = GeneratePos(unitList)
    atk = TotalAtkCount(kromD)
    selisih = atk[1] - atk[0]
    var = (kromD, selisih)
    fullList.append(var)

    step = 0
    while step<1 or step>1000000:
        step = int(input("Jumlah step: "))
        
    for i in range (step):
        fullList.sort(key=lambda tup : tup[1], reverse=True) # sort by fitness function
        
        while (len(fullList)>4):
            fullList.remove(fullList[4])
        
        cross1 = []
        cross2 = []

        krom = fullList[0][0]
        cross1.append(copy.deepcopy(krom))
    
        krom = fullList[1][0]
        cross1.append(copy.deepcopy(krom))
        cross2.append(copy.deepcopy(krom))

        krom = fullList[2][0]
        cross2.append(copy.deepcopy(krom))

        #selection
        s1= random.randint(1, len(kromA) -1)
        s2= random.randint(1, len(kromA) -1)
        awal1 = cross1.pop(0) #paling optimal
        akhir1 = cross1.pop(0) #kedua optimal
        awal11 = []
        akhir11 = []
        for j in range (0, s1):
            awal11.append(awal1.pop(0))
            akhir11.append(akhir1.pop(0))
        kromA = []
        kromA = awal11 + akhir1
        kromB = []
        kromB = akhir11 + awal1

        awal2 = cross2.pop(0)
        akhir2 = cross2.pop(0)
        awal22 = []
        akhir22 = []
        for j in range (0, s2):
            awal22.append(awal2.pop(0))
            akhir22.append(akhir2.pop(0))
        kromC = []
        kromC = awal22 + akhir2
        kromD = []
        kromD = akhir22 + awal2
        
        j = 0
        mutasi = False
        for A in kromA:
            temporaryList = []
            temporaryList = kromA.copy()
            temporaryList.remove(A)
            if not (AvailCheck(A[2], A[3], temporaryList)) :
                semen = list(kromA[j])
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                while not (AvailCheck(x, y, temporaryList)) :
                    x = random.randint(0, 7)
                    y = random.randint(0, 7)    
                semen[2] = x
                semen[3] = y
                tup = tuple(semen)
                kromA[j] = tup
                mutasi = True
            j = j + 1
        if not mutasi :
            temp = random.randint(0, len(kromA)-1)
            semen = list(kromA[temp])
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while not (AvailCheck(x, y, kromA)) :
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            semen[2] = x
            semen[3] = y
            tup = tuple(semen)
            kromA[temp] = tup
            
        j = 0
        mutasi = False
        for B in kromB:
            temporaryList = []
            temporaryList = kromB.copy()
            temporaryList.remove(B)
            if not (AvailCheck(B[2], B[3], temporaryList)) :
                semen = list(kromB[j])
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                while not (AvailCheck(x, y, temporaryList)) :
                    x = random.randint(0, 7)
                    y = random.randint(0, 7)    
                semen[2] = x
                semen[3] = y
                tup = tuple(semen)
                kromB[j] = tup
                mutasi = True
            j = j + 1
        if not mutasi :
            temp = random.randint(0, len(kromB)-1)
            semen = list(kromB[temp])
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while not (AvailCheck(x, y, kromB)) :
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            semen[2] = x
            semen[3] = y
            tup = tuple(semen)
            kromB[temp] = tup
            
        j = 0
        mutasi = False
        for C in kromC:
            temporaryList = []
            temporaryList = kromC.copy()
            temporaryList.remove(C)
            if not (AvailCheck(C[2], C[3], temporaryList)) :
                semen = list(kromC[j])
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                while not (AvailCheck(x, y, temporaryList)) :
                    x = random.randint(0, 7)
                    y = random.randint(0, 7)    
                semen[2] = x
                semen[3] = y
                tup = tuple(semen)
                kromC[j] = tup
                mutasi = True
            j = j + 1
        if not mutasi :
            temp = random.randint(0, len(kromC)-1)
            semen = list(kromC[temp])
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while not (AvailCheck(x, y, kromC)) :
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            semen[2] = x
            semen[3] = y
            tup = tuple(semen)
            kromC[temp] = tup
            
        j = 0
        mutasi = False
        for D in kromD:
            temporaryList = []
            temporaryList = kromD.copy()
            temporaryList.remove(D)
            if not (AvailCheck(D[2], D[3], temporaryList)) :
                semen = list(kromD[j])
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                while not (AvailCheck(x, y, temporaryList)) :
                    x = random.randint(0, 7)
                    y = random.randint(0, 7)    
                semen[2] = x
                semen[3] = y
                tup = tuple(semen)
                kromD[j] = tup
                mutasi = True
            j = j + 1
        if not mutasi :
            temp = random.randint(0, len(kromD)-1)
            semen = list(kromD[temp])
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            while not (AvailCheck(x, y, kromD)) :
                x = random.randint(0, 7)
                y = random.randint(0, 7)
            semen[2] = x
            semen[3] = y
            tup = tuple(semen)
            kromD[temp] = tup
            
        atkCount = TotalAtkCount(kromA)
        selisih = atkCount[1] - atkCount[0]
        temp = (kromA, selisih)
        fullList.append(temp)
        
        atkCount = TotalAtkCount(kromB)
        selisih = atkCount[1] - atkCount[0]
        temp = (kromB, selisih)
        fullList.append(temp)
        
        atkCount = TotalAtkCount(kromC)
        selisih = atkCount[1] - atkCount[0]
        temp = (kromC, selisih)
        fullList.append(temp)
        
        atkCount = TotalAtkCount(kromD)
        selisih = atkCount[1] - atkCount[0]
        temp = (kromD, selisih)
        fullList.append(temp)

    fullList.sort(key=lambda tup : tup[1], reverse=True)
    return fullList[0][0]

if __name__ == "__main__" :
    #inisiasi
    fileName = input('Nama File : ')
    unitList = ReadFile(fileName)

    papanKosong = False
    ulang = True
    while ulang :
        valid = False
        while not valid :
            #menu
            print("Pilih algoritma local search yang kamu inginkan :")
            print("1. Hill Climb")
            print("2. Simulated Annealing")
            print("3. Genetic Algorithm")
            pilihan = input("Pilihanmu : ")

            if pilihan == "1" :
                #Hill Climb
                tempList = hill_climbing(unitList)
                if not tempList :
                    papanKosong = True
                else :
                    count = TotalAtkCount(tempList)
                valid = True

            elif pilihan == "2" :
                #Simulated Annealing
                tempList = simulatedAnnealing(unitList)
                if not tempList :
                    papanKosong = True
                else :
                    count = TotalAtkCount(tempList)
                valid = True
            elif pilihan == "3" :
                #Genetic Algorithm
                tempList = geneticAlgorithm(unitList)
                if not tempList :
                    papanKosong = True
                else :
                    count = TotalAtkCount(tempList)
                valid = True
            else :
                print("Pilihan tidak valid")

        if papanKosong :
            print("Maaf papan kosong, tidak ada yang bisa diproses")
            valid = True
            ulang = False
        else :
            valid = False
            #menampilkan solusi
            print("Solusi :")
            PrintBoard(tempList)
            print(count[0], count[1])

        while not valid :
            print("Masih mau coba lagi? (y/n)")
            pilihan = input()
            if pilihan == "n" or pilihan == "N" :
                print("Terima kasih telah menggunakan program kami")
                print("Program ini diciptakan oleh: ")
                print("1. Nira Rizki R - 13516018")
                print("2. Irfan Ihsanul A - 13516064")
                print("3. M Azka Widyanto - 13516127")
                print("4. Nadija Herdwina P S - 13516130")
                print("5. Trian Annas T S - 13516148")
                valid = True
                ulang = False
            elif pilihan == "y" or pilihan == "Y" :
                valid = True
            else :
                print("Pilihan tidak valid")
