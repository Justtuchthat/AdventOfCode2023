INPUTFILENAME = "input"
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def processLine(line):
    firstNum = -1
    lastNum = -1
    for i in range(len(line)):
        if line[i] in digits:
            lastNum = int(line[i])
            if firstNum == -1:
                firstNum = lastNum
    print("firstnum = ", firstNum, ", lastnum = ", lastNum)
    return firstNum*10 + lastNum

def main():
    with open(INPUTFILENAME, 'r') as input:
        total = 0
        for line in input:
            print("The line is:\n", line)
            total += processLine(line)
        print(total)

if __name__ == "__main__":
    main()