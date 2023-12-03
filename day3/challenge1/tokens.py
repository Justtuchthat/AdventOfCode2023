digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Item:
    def isNumber(self):
        return False
    
    def isEmpty(self):
        return False
    
    def isSymbol(self):
        return False
    
    def symbolNextToMe(self):
        pass

    def countMe(self):
        return 0

class Number(Item):
    def __init__(self, val):
        self.isCounted = False # set to True once this number is counted in the total
        self.isNextToSymbol = False
        self.val = val
    
    def symbolNextToMe(self):
        self.isNextToSymbol = True
    
    def countMe(self):
        if not self.isNextToSymbol:
            return 0
        if self.isCounted:
            return 0
        self.isCounted = True
        return self.val
    
    def isNumber(self):
        return True

class Empty(Item):
    def isEmpty(self):
        return True

class Symbol(Item):
    def isSymbol(self):
        return True

def indexNoError(array, idx):
    try:
        return array[idx]
    except IndexError:
        return None

def tokenizeSchematic(schematic):
    tokenGrid = []
    for line in schematic:
        nextTokenLine = []
        i = 0
        while i <len(line):
            if line[i] == ".":
                nextTokenLine.append(Empty())
            elif line[i] in digits:
                value = int(line[i])
                numLen = 1
                while indexNoError(line, i+1) in digits:
                    i += 1
                    numLen += 1
                    value *= 10
                    value += int(line[i])
                num = Number(value)
                for _ in range(numLen):
                    nextTokenLine.append(num)
            else:
                nextTokenLine.append(Symbol())
            i += 1
        tokenGrid.append(nextTokenLine)
    return tokenGrid

