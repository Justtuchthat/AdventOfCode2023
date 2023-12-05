import readInput

INPUTFILENAME = "input"


def readMap(mapList: 'list[tuple[range, int]]', source: 'int')->'int':
    for r, diff in mapList:
        if source in r:
            return source+diff
    return source


def main():
    inputLines = []
    with open(INPUTFILENAME, 'r') as file:
        for line in file:
            inputLines.append(line)
    seedsList, inputRest = readInput.readSeeds(inputLines)
    seed2soil, inputRest = readInput.readMap(inputRest)
    soils = []
    for seed in seedsList:
        soils.append(readMap(seed2soil, seed))
    soil2fert, inputRest = readInput.readMap(inputRest)
    ferts = []
    for soil in soils:
        ferts.append(readMap(soil2fert, soil))
    fert2wate, inputRest = readInput.readMap(inputRest)
    wates = []
    for fert in ferts:
        wates.append(readMap(fert2wate, fert))
    wate2ligh, inputRest = readInput.readMap(inputRest)
    lighs = []
    for wate in wates:
        lighs.append(readMap(wate2ligh, wate))
    ligh2temp, inputRest = readInput.readMap(inputRest)
    temps = []
    for ligh in lighs:
        temps.append(readMap(ligh2temp, ligh))
    temp2humi, inputRest = readInput.readMap(inputRest)
    humis = []
    for temp in temps:
        humis.append(readMap(temp2humi, temp))
    humi2loca, inputRest = readInput.readMap(inputRest)
    locas = []
    for humi in humis:
        locas.append(readMap(humi2loca, humi))
    print(min(locas))


if __name__ == "__main__":
    main()