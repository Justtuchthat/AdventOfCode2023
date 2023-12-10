INPUTFILENAME = "input"


def getPreviousSteps(history: 'list[list[int]]') -> 'list[list[int]]':
    while sum(history[-1]) != 0:
        prevStep = []
        for i in range(1, len(history[-1])):
            prevStep.append(history[-1][i] - history[-1][i-1])
        history.append(prevStep)
    return history


def extrapolateNewData(history: 'list[list[int]]') -> 'list[list[int]]':
    for line in history:
        line[:0] = [0]
    for i in range(len(history)-2, -1, -1):
        history[i][0] = history[i][1]-history[i+1][0]
    return history


def main():
    histories = []
    with open(INPUTFILENAME, 'r') as input:
        for line in input:
            histories.append([[int(x) for x in line.strip().split(' ')]])
    
    newData = []
    for history in histories:
        newData.append(extrapolateNewData(getPreviousSteps(history)))
    totalNew = 0
    for history in histories:
        totalNew += history[0][0]
    print(totalNew)

    
    
            

if __name__ == "__main__":
    main()