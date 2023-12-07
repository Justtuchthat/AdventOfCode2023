import readInput

INPUTFILENAME = "input"



def singleMapSegment(mapSeg, sourceRange):
    print("Reading map seg: ", mapSeg, " with range ", sourceRange)
    mapSegStart = mapSeg[0][0]
    mapSegEnd = mapSeg[0][1]
    diff = mapSeg[1]
    mapRange = range(mapSegStart, mapSegEnd)
    if sourceRange[0] in mapRange: # if source range starts in mapRange
        if sourceRange[1] in mapRange: # and ends in mapRange
            return (sourceRange[0]+diff, sourceRange[1]+diff), None
        # now end is out of range
        newRange = (sourceRange[0]+diff, mapSegEnd+diff)
        sourceRange = (mapSegEnd, sourceRange[1])
        return newRange, sourceRange
    # source range start is out of mapRange
    if sourceRange[1] in mapRange:
        # source range end is in mapRange
        newRange = (mapSegStart+diff, sourceRange[1]+diff)
        sourceRange = (sourceRange[0], mapSegStart)
        return newRange, sourceRange
    # source range is entirely out of range
    return None, sourceRange

def readMap(mapList, sourceRange):
    returnRange = []
    for mapSeg in mapList:
        if sourceRange is None:
            return returnRange
        newRange, sourceRange = singleMapSegment(mapSeg, sourceRange)
        if newRange is not None:
            returnRange.append(newRange)
    if sourceRange is not None:
        returnRange.append(sourceRange)
    return returnRange

def fixRangeList(list):
    return [(a,b) for a,b in list if a != b]

def main():
    inputLines = []
    with open(INPUTFILENAME, 'r') as file:
        for line in file:
            inputLines.append(line)
    seedsList, inputRest = readInput.readSeeds(inputLines)
    seed2soil, inputRest = readInput.readMap(inputRest)
    soils = []
    print("Seeds", seedsList)
    print(seed2soil)
    for seed in seedsList:
        soils.extend(readMap(seed2soil, seed))
    soils = fixRangeList(soils)
    print("Soils", soils)
    soil2fert, inputRest = readInput.readMap(inputRest)
    ferts = []
    print(soil2fert)
    for soil in soils:
        ferts.extend(readMap(soil2fert, soil))
    ferts = fixRangeList(ferts)
    print("Fertilizers", ferts)
    fert2wate, inputRest = readInput.readMap(inputRest)
    wates = []
    print(fert2wate)
    for fert in ferts:
        wates.extend(readMap(fert2wate, fert))
    wates = fixRangeList(wates)
    print("Waters", wates)
    wate2ligh, inputRest = readInput.readMap(inputRest)
    lighs = []
    print(wate2ligh)
    for wate in wates:
        lighs.extend(readMap(wate2ligh, wate))
    lighs = fixRangeList(lighs)
    print("Lights", lighs)
    ligh2temp, inputRest = readInput.readMap(inputRest)
    temps = []
    print(ligh2temp)
    for ligh in lighs:
        temps.extend(readMap(ligh2temp, ligh))
    temps = fixRangeList(temps)
    print("Temps", temps)
    temp2humi, inputRest = readInput.readMap(inputRest)
    humis = []
    print(temp2humi)
    for temp in temps:
        humis.extend(readMap(temp2humi, temp))
    humis = fixRangeList(humis)
    print("Humidities", humis)
    humi2loca, inputRest = readInput.readMap(inputRest)
    locas = []
    print(humi2loca)
    for humi in humis:
        locas.extend(readMap(humi2loca, humi))
    locas = fixRangeList(locas)
    print("Locations", locas)
    print(min([item[0] for item in locas]))


if __name__ == "__main__":
    main()