from galaxy import processLine, isEmptyRow, increaseRow, increaseCol
import itertools


INPUTFILENAME = "input"


blowupSize = 1_000_000
blowupSize -= 1


def manhattanDistance(g1, g2):
    return abs(g1.x - g2.x) + abs(g1.y - g2.y)


def main():
    image = []
    with open(INPUTFILENAME, 'r') as input:
        for row, line in enumerate(input):
            image.append(processLine(line, row))
    increase = 0
    for row in image:
        if isEmptyRow(row):
            increase += blowupSize
            continue
        increaseRow(row, increase)
    increase = 0
    for i in range(len(image[0])):
        col = [row[i] for row in image]
        if isEmptyRow(col):
            increase += blowupSize
            continue
        increaseCol(col, increase)
    galaxies = []
    for row in image:
        galaxies.extend([galaxy for galaxy in row if galaxy.isGalaxy()])
    totalDistance = 0
    for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
        totalDistance += manhattanDistance(galaxy1, galaxy2)
    print(totalDistance)


if __name__ == "__main__":
    main()