from pipes import processLine, PipeType, Pipe

INPUTFILENAME = "input"

def floodFill(pipeGrid, indexes):
    while len(indexes) > 0:
        i, j = indexes[0]
        del indexes[0]
        if pipeGrid[i][j].isVisited():
            continue
        pipeGrid[i][j].visit()
        match pipeGrid[i][j].type:
            case PipeType.VERTICAL:
                indexes.extend([(i-1,j),(i+1,j)])
            case PipeType.HORIZONTAL:
                indexes.extend([(i,j-1),(i,j+1)])
            case PipeType.TOPTORIGHT:
                indexes.extend([(i-1,j),(i,j+1)])
            case PipeType.TOPTOLEFT:
                indexes.extend([(i-1,j),(i,j-1)])
            case PipeType.BOTTOMTOLEFT:
                indexes.extend([(i+1,j),(i,j-1)])
            case PipeType.BOTTOMTORIGHT:
                indexes.extend([(i+1,j),(i,j+1)])


def invsoutLine(line):
    i = 0
    outside = True
    switch = lambda x: False if x else True
    needUp = False
    needDown = False
    while i < len(line):
        match line[i].type:
            case PipeType.GROUND:
                line[i].outside = outside
            case PipeType.VERTICAL:
                outside = switch(outside)
            case PipeType.TOPTORIGHT:
                needDown = True
            case PipeType.BOTTOMTORIGHT:
                needUp = True
            case PipeType.BOTTOMTOLEFT:
                if needDown:
                    outside = switch(outside)
                needUp = False
                needDown = False
            case PipeType.TOPTOLEFT:
                if needUp:
                    outside = switch(outside)
                needUp = False
                needDown = False
        i += 1


def main():
    pipeGrid = []
    with open(INPUTFILENAME, 'r') as input:
        for line in input:
            pipeGrid.append(processLine(line.strip()))
    startLoc = PipeType.matchStartType(pipeGrid)
    floodFill(pipeGrid, [startLoc])
    pipeGrid = [[pipe if pipe.isVisited() else Pipe('.') for pipe in pipeLine] for pipeLine in pipeGrid]
    for pipeLine in pipeGrid:
        invsoutLine(pipeLine)
    pipeGrid = [[1 if pipe.isInside() else 0 for pipe in line] for line in pipeGrid]
    print(sum([sum(x) for x in pipeGrid]))
    


if __name__ == "__main__":
    main()