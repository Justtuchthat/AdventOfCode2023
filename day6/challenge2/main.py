INPUTFILENAME = "input"


def calculateWins(time, recDist):
    for i in range(time+1):
        remainingTime = time-i
        dist = remainingTime*i
        if dist > recDist:
            return time-2*i+1


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
    times = [str(time) for time in times]
    distances = [str(dist) for dist in distances]
    times = [int(''.join(times))]
    distances = [int(''.join(distances))]

    marginOfError = 1
    for time, recDist in zip(times, distances):
        wins = calculateWins(time, recDist)
        marginOfError *= wins
    print(marginOfError)
    


if __name__ == "__main__":
    main()