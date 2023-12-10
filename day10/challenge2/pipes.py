from enum import Enum

class PipeType(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    TOPTORIGHT = 2
    TOPTOLEFT = 3
    BOTTOMTORIGHT = 4
    BOTTOMTOLEFT = 5
    GROUND = 6
    START = 7

    def getPipeType(c):
        match c:
            case '.':
                return PipeType.GROUND
            case '|':
                return PipeType.VERTICAL
            case '-':
                return PipeType.HORIZONTAL
            case 'L':
                return PipeType.TOPTORIGHT
            case 'J':
                return PipeType.TOPTOLEFT
            case '7':
                return PipeType.BOTTOMTOLEFT
            case 'F':
                return PipeType.BOTTOMTORIGHT
            case 'S':
                return PipeType.START
    
    def matchStartType(pipeGrid):
        for i in range(len(pipeGrid)):
            for j in range(len(pipeGrid[i])):
                if pipeGrid[i][j].type == PipeType.START:
                    top = getNoError2d(pipeGrid, i-1, j)
                    left = getNoError2d(pipeGrid, i, j-1)
                    right = getNoError2d(pipeGrid, i, j+1)
                    bottom = getNoError2d(pipeGrid, i+1, j)
                    if top.type == PipeType.VERTICAL or\
                       top.type == PipeType.BOTTOMTOLEFT or\
                       top.type == PipeType.BOTTOMTORIGHT:
                        top = True
                    else:
                        top = False
                    if left.type == PipeType.HORIZONTAL or\
                       left.type == PipeType.TOPTORIGHT or\
                       left.type == PipeType.BOTTOMTORIGHT:
                        left = True
                    else:
                        left = False
                    if bottom.type == PipeType.VERTICAL or\
                       bottom.type == PipeType.TOPTORIGHT or\
                       bottom.type == PipeType.TOPTOLEFT:
                        bottom = True
                    else:
                        bottom = False
                    if right.type == PipeType.HORIZONTAL or\
                       right.type == PipeType.TOPTOLEFT or\
                       right.type == PipeType.BOTTOMTOLEFT:
                        right = True
                    else:
                        right = False
                    if top and left:
                        pipeGrid[i][j] = Pipe('J')
                    elif top and bottom:
                        pipeGrid[i][j] = Pipe('|')
                    elif top and right:
                        pipeGrid[i][j] = Pipe('L')
                    elif bottom and left:
                        pipeGrid[i][j] = Pipe('7')
                    elif bottom and right:
                        pipeGrid[i][j] = Pipe('F')
                    elif left and right:
                        pipeGrid[i][j] = Pipe('-')
                    return i,j


class Pipe:
    def __init__(self, char):
        self.type = PipeType.getPipeType(char)
        self.char = char
        self.visited = False
        self.outside = None
    
    def isVisited(self):
        return self.visited
    
    def visit(self):
        self.visited = True

    def isInside(self):
        if self.type != PipeType.GROUND:
            return False
        return not self.outside


def getNoError2d(array, i, j):
    try:
        return array[i][j]
    except IndexError:
        return None


def processLine(line):
    pipeLine = []
    for c in line:
        pipeLine.append(Pipe(c))
    return pipeLine