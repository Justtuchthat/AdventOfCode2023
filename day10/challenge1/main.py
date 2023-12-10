from pipes import processLine, PipeType, getNoError2d, Pipe
import pipes


INPUTFILENAME = "input"


def floodFill(pipeGrid, indexes):
    while len(indexes) > 0:
        i, j = indexes[0]
        del indexes[0]
        if pipeGrid[i][j].isVisited():
            continue
        pipeGrid[i][j].visit()
        top = getNoError2d(pipeGrid, i-1, j)
        left = getNoError2d(pipeGrid, i, j-1)
        right = getNoError2d(pipeGrid, i, j+1)
        bottom = getNoError2d(pipeGrid, i+1, j)
        dist = -1
        match pipeGrid[i][j].type:
            case PipeType.VERTICAL:
                indexes.extend([(i-1,j),(i+1,j)])
                dist = min(top.dist, bottom.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
            case PipeType.HORIZONTAL:
                indexes.extend([(i,j-1),(i,j+1)])
                dist = min(left.dist, right.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
            case PipeType.TOPTORIGHT:
                indexes.extend([(i-1,j),(i,j+1)])
                dist = min(top.dist, right.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
            case PipeType.TOPTOLEFT:
                indexes.extend([(i-1,j),(i,j-1)])
                dist = min(top.dist, left.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
            case PipeType.BOTTOMTOLEFT:
                indexes.extend([(i+1,j),(i,j-1)])
                dist = min(bottom.dist, left.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
            case PipeType.BOTTOMTORIGHT:
                indexes.extend([(i+1,j),(i,j+1)])
                dist = min(bottom.dist, right.dist) + 1
                dist = dist if dist != float('inf') else 0
                pipeGrid[i][j].dist = dist
    pass


def main():
    pipeGrid = []
    with open(INPUTFILENAME, 'r') as input:
        for line in input:
            pipeGrid.append(processLine(line.strip()))
    startLoc = PipeType.matchStartType(pipeGrid)
    floodFill(pipeGrid, [startLoc])
    dists = [[a.dist if a.dist != float('inf') else -1 for a in line] for line in pipeGrid]
    print(max([max(a) for a in dists]))


if __name__ == "__main__":
    main()