INPUTFILENAME = "input"

def getGamePower(gameData):
    leastRedNeeded = 0
    leastGreenNeeded = 0
    leastBlueNeeded = 0
    for hand in gameData.split("; "):
        for set in hand.split(', '):
            match set.split(' '):
                case [val, "red"]:
                    leastRedNeeded = max(int(val), leastRedNeeded)
                case [val, "green"]:
                    leastGreenNeeded = max(int(val), leastGreenNeeded)
                case [val, "blue"]:
                    leastBlueNeeded = max(int(val), leastBlueNeeded)
                case _:
                    Exception("Not RGB set in hand?")
    return leastRedNeeded*leastGreenNeeded*leastBlueNeeded
        

def main():
    with open(INPUTFILENAME, 'r') as input:
        total = 0
        for line in input:
            gameName, gameData = line.split(': ')
            _, gameID = gameName.split(' ')
            total += getGamePower(gameData.strip())
        print(total)

if __name__ == "__main__":
    main()