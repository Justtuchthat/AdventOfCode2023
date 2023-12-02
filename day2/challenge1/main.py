INPUTFILENAME = "input"

def isPossibleGame(gameData):
    for hand in gameData.split("; "):
        totalRed = 0
        totalGreen = 0
        totalBlue = 0
        for set in hand.split(', '):
            match set.split(' '):
                case [val, "red"]:
                    totalRed += int(val)
                case [val, "green"]:
                    totalGreen += int(val)
                case [val, "blue"]:
                    totalBlue += int(val)
                case _:
                    Exception("Not RGB set in hand?")
        if totalRed > 12:
            return False
        if totalGreen > 13:
            return False
        if totalBlue > 14:
            return False
    return True

def main():
    with open(INPUTFILENAME, 'r') as input:
        total = 0
        for line in input:
            gameName, gameData = line.split(': ')
            _, gameID = gameName.split(' ')
            if isPossibleGame(gameData.strip()):
                print("Adding game ", gameID)
                total += int(gameID)
        print(total)

if __name__ == "__main__":
    main()