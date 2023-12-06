INPUTFILENAME = "test"


def calculatePossibilities(time):
    distances = []
    for i in range(time+1):
        remainingTime = time-i
        dist = remainingTime*i
        distances.append(dist)
    return distances


def main():
    times = []
    distances =[]
    with open(INPUTFILENAME, 'r') as file:
        for line in file:
            words = line.split(':')
            if words[0] == "Time":
                times = [int(time) for time in words[1].strip().split(' ') if time]
            if words[0] == "Distance":
                distances = [int(dist) for dist in words[1].strip().split(' ') if dist]

    marginOfError = 1
    for time, recDist in zip(times, distances):
        print("Record for ", time, " is ", recDist)
        possibleDists = calculatePossibilities(time)
        totalWinning = sum(map(lambda dist: 1 if dist > recDist else 0, possibleDists))
        marginOfError *= totalWinning
    print(marginOfError)
    


if __name__ == "__main__":
    main()