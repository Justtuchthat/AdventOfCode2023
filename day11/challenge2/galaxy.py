class Pixel:
    def isGalaxy(self):
        return False
    
    def isEmpty(self):
        return False

class Galaxy(Pixel):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Galaxy("+ str(self.x) + ", " + str(self.y) + ")"
    
    def isGalaxy(self):
        return True

class Empty(Pixel):
    def isEmpty(self):
        return True

def processLine(line, row):
    pixelLine = []
    for col, let in enumerate(line):
        match let:
            case '.':
                pixelLine.append(Empty())
            case '#':
                pixelLine.append(Galaxy(row, col))
    return pixelLine

def isEmptyRow(row):
    for pixel in row:
        if pixel.isGalaxy():
            return False
    return True

def increaseRow(row, increase):
    for pixel in row:
        if pixel.isGalaxy():
            pixel.x += increase

def increaseCol(col, increase):
    for pixel in col:
        if pixel.isGalaxy():
            pixel.y += increase