INPUTFILENAME = "input"

def main():
    with open(INPUTFILENAME, 'r') as input:
        totalPoints = 0
        for line in input:
            gameNums = line.strip().split(": ")[1].split(" | ")
            winningNums = [int(x) for x in gameNums[1].split(" ") if x != '']
            cardNums = [int(x) for x in gameNums[0].split(" ") if x != '']
            winNumsOnThisCard = [num for num in cardNums if num in winningNums]
            power = len(winNumsOnThisCard)-1
            totalPoints += int(2**power)
        print(totalPoints)

if __name__ == "__main__":
    main()