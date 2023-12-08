INPUTFILENAME = "input"


def main():
    nodesToNodes = {}
    walkingInstructions = None
    with open(INPUTFILENAME, 'r') as input:
        for line in input:
            if walkingInstructions is None:
                walkingInstructions = line.strip()
            elif line == '\n':
                continue
            else:
                key = line.strip().split(" = ")[0]
                nodes = line.strip().split(" = ")[1][1:-1].split(", ")
                nodesToNodes[key] = (nodes[0], nodes[1])
    currentNode = 'AAA'
    wlkInsTimesRead = 0
    while currentNode != 'ZZZ':
        for let in walkingInstructions:
            nodeMap = nodesToNodes[currentNode]
            match let:
                case 'R':
                    currentNode = nodeMap[1]
                case 'L':
                    currentNode = nodeMap[0]
        wlkInsTimesRead += 1
    print(len(walkingInstructions) * wlkInsTimesRead)
            

if __name__ == "__main__":
    main()