class Hotspring:
    def __init__(self, line):
        self.hotsprings = list(line.split(' ')[0])
        self.nums = [int(x) for x in line.split(' ')[1].split(',')]
    
    def getNumArrangements(self):
        if (i := self.getFirstQuestionMark()) == -1:
            return 1 if self.isCorrect() else 0
        self.hotsprings[i] = '.'
        totalPossible = self.getNumArrangements()
        self.hotsprings[i] = '#'
        totalPossible += self.getNumArrangements()
        self.hotsprings[i] = '?'
        return totalPossible
    
    def getFirstQuestionMark(self):
        for i, let in enumerate(self.hotsprings):
            if let == '?':
                return i
        return -1
    
    def isCorrect(self):
        curRange = 0
        ranges = []
        for let in self.hotsprings:
            if let == '#':
                curRange += 1
            elif let == '.' and curRange > 0:
                ranges.append(curRange)
                curRange = 0
        if curRange > 0:
            ranges.append(curRange)
        return ranges == self.nums
