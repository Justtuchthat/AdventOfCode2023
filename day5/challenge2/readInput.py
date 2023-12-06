

def readSeeds(inputLines: 'list[str]'):
    seeds = inputLines[0].split(': ')[1].strip()
    seeds = [int(seed) for seed in seeds.split(" ")]
    totalSeeds = []
    idx = 0
    while idx < len(seeds):
        start = seeds[idx]
        length = seeds[idx+1]
        totalSeeds.append((start, start+length-1))
        idx += 2
    return totalSeeds, inputLines[2:]

def makeRangeEntry(line: 'str'):
    nums = [int(x) for x in line.strip().split(' ')]
    dst = nums[1]
    src = nums[0]
    rlen = nums[2]
    return (dst, dst+rlen-1), src-dst

def readMap(inputLines: 'list[str]'):
    rangeMap: 'list[tuple[tuple[int, int], int]]' = []
    idx = 1
    while (idx < len(inputLines)) and inputLines[idx] != '\n':
        rangeMap.append(makeRangeEntry(inputLines[idx]))
        idx += 1
    return sorted(rangeMap), inputLines[idx+1:]