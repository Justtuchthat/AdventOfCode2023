from tokens import tokenizeSchematic

INPUTFILENAME = "input"

def isPossible(tokenGrid, x, y):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= len(tokenGrid):
        return False
    if y >= len(tokenGrid[x]):
        return False
    return True


def notifyNeighboursOfSymbol(tokenGrid, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if isPossible(tokenGrid, x+i, y+j):
                tokenGrid[x+i][y+j].symbolNextToMe()


def processSymbols(tokenGrid):
    for x in range(len(tokenGrid)):
        for y in range(len(tokenGrid[x])):
            if tokenGrid[x][y].isSymbol():
                notifyNeighboursOfSymbol(tokenGrid, x, y)


def countPartNumbers(tokenGrid):
    total = 0
    for line in tokenGrid:
        for token in line:
            total += token.countMe()
    return total


def main():
    with open(INPUTFILENAME, 'r') as input:
        schematic = []
        for line in input:
            schematic.append(line.strip())
        tokenGrid = tokenizeSchematic(schematic)
        processSymbols(tokenGrid)
        print(countPartNumbers(tokenGrid))


if __name__ == "__main__":
    main()