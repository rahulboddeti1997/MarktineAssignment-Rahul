noOfGrids = int(input())
villageGrids = list(input())

def splitHouses(noOfGrids,villageGrids):
    for i in range(noOfGrids):
        if i < noOfGrids-1:
            if villageGrids[i] == 'H' and villageGrids[i+1] == 'H' :
                print("NO");
                return
        if villageGrids[i] == ".":
            villageGrids[i] = "B";
    print("YES");
    print("".join(villageGrids));
    
splitHouses(noOfGrids,villageGrids);