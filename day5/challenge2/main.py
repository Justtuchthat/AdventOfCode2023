import readInput

INPUTFILENAME = "test"

def findMapIdx(mapList, num):
    for i in range(len(mapList)):
        if num < mapList[i][0][0]:
            return -1
        if num > mapList[i][0][0] and num < mapList[i][0][1]:
            return i
    return -1

def readMap(mapList, sourceRange):
    returnRange = []
    sbeg, send = sourceRange
    sbegMapIdx = findMapIdx(mapList, sbeg)
    sendMapIdx = findMapIdx(mapList, send)
    print(sourceRange, mapList, sbegMapIdx, sendMapIdx)
    if sbegMapIdx == sendMapIdx:
        dif = mapList[sbegMapIdx][1]
        return [(sbeg+dif, send+dif)]
    
    return []

def main():
    inputLines = []
    with open(INPUTFILENAME, 'r') as file:
        for line in file:
            inputLines.append(line)
    seedsList, inputRest = readInput.readSeeds(inputLines)
    seed2soil, inputRest = readInput.readMap(inputRest)
    soils = []
    for seed in seedsList:
        soils.extend(readMap(seed2soil, seed))
    print(seedsList)
    print(seed2soil)
    print(soils)
    soil2fert, inputRest = readInput.readMap(inputRest)
    ferts = []
    for soil in soils:
        ferts.extend(readMap(soil2fert, soil))
    print(ferts)
    fert2wate, inputRest = readInput.readMap(inputRest)
    wates = []
    for fert in ferts:
        wates.extend(readMap(fert2wate, fert))
    print(wates)
    wate2ligh, inputRest = readInput.readMap(inputRest)
    lighs = []
    for wate in wates:
        lighs.extend(readMap(wate2ligh, wate))
    print(lighs)
    ligh2temp, inputRest = readInput.readMap(inputRest)
    temps = []
    for ligh in lighs:
        temps.extend(readMap(ligh2temp, ligh))
    print(temps)
    temp2humi, inputRest = readInput.readMap(inputRest)
    humis = []
    for temp in temps:
        humis.extend(readMap(temp2humi, temp))
    print(humis)
    humi2loca, inputRest = readInput.readMap(inputRest)
    locas = []
    for humi in humis:
        locas.extend(readMap(humi2loca, humi))
    print(locas)


if __name__ == "__main__":
    main()