INPUTFILENAME = "input"


def isStartingNode(node):
    return node[-1] == 'A'


def isFinishingState(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True


def getLenWalkingList(node, nodeMap, walkingInstructions):
    totalLen = 0
    while node[-1] != 'Z':
        for let in walkingInstructions:
            nodeIns = nodeMap[node]
            match let:
                case 'R':
                    node = nodeIns[1]
                case 'L':
                    node = nodeIns[0]
        totalLen += 1
    return totalLen * len(walkingInstructions)


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def LCM(a, b):
    return a*b//GCD(a, b)


def main():
    nodesToNodes = {}
    startingNodes = []
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
                if isStartingNode(key):
                    startingNodes.append(key)
    nodeLens = []
    for node in startingNodes:
        nodeLens.append(getLenWalkingList(node, nodesToNodes, walkingInstructions))
    print(nodeLens)
    currLen = 1
    for nodeLen in nodeLens:
        currLen = LCM(currLen, nodeLen)
    print(currLen)
    
            

if __name__ == "__main__":
    main()