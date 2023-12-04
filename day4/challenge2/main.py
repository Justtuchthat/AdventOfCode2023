INPUTFILENAME = "input"

def addCopies(winNumsArr, idx, totalCopiesToAdd):
    if idx >= len(winNumsArr):
        return
    winNumsArr[idx][1] += totalCopiesToAdd

def main():
    with open(INPUTFILENAME, 'r') as file:
        winningNumbersOnCards = []
        input = []
        for line in file:
            input.append(line)
        for i in range(len(input)):
            gameNums = input[i].strip().split(": ")[1].split(" | ")
            winningNums = [int(x) for x in gameNums[1].split(" ") if x != '']
            cardNums = [int(x) for x in gameNums[0].split(" ") if x != '']
            winNumsOnThisCard = [num for num in cardNums if num in winningNums]
            winningNumbersOnCards.append([winNumsOnThisCard, 1, i+1])
        for i in range(len(winningNumbersOnCards)):
            copies = winningNumbersOnCards[i][1]
            wins = winningNumbersOnCards[i][0]
            wins = len(wins)
            while wins > 0:
                addCopies(winningNumbersOnCards, i + wins, copies)
                wins -= 1
        print(sum([x[1] for x in winningNumbersOnCards]))

if __name__ == "__main__":
    main()