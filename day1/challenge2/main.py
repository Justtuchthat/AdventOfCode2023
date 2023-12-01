INPUTFILENAME = "input"
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get(line, i):
    try:
        return line[i]
    except IndexError:
        return None

def startFrom(line, sub, idx):
    for i in range(len(sub)):
        if not get(line, idx+i)==sub[i]:
            return False
    return True

def num(line, i):
    if line[i] in digits:
        return int(line[i])
    if startFrom(line, 'one', i):
        return 1
    if startFrom(line, 'two', i):
        return 2
    if startFrom(line, 'three', i):
        return 3
    if startFrom(line, 'four', i):
        return 4
    if startFrom(line, 'five', i):
        return 5
    if startFrom(line, 'six', i):
        return 6
    if startFrom(line, 'seven', i):
        return 7
    if startFrom(line, 'eight', i):
        return 8
    if startFrom(line, 'nine', i):
        return 9
    return None

def processLine(line):
    firstNum = -1
    lastNum = -1
    for i in range(len(line)):
        numAti = num(line, i)
        if numAti is not None:
            lastNum = numAti
            if firstNum == -1:
                firstNum = lastNum
    return firstNum*10 + lastNum

def main():
    with open(INPUTFILENAME, 'r') as input:
        total = 0
        for line in input:
            total += processLine(line)
        print(total)

if __name__ == "__main__":
    main()