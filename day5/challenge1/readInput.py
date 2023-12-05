

def readSeeds(inputLines: 'list[str]'):
    seeds = inputLines[0].split(': ')[1].strip()
    seeds = [int(seed) for seed in seeds.split(" ")]
    return seeds, inputLines[2:]

def makeRangeEntry(line: 'str'):
    nums = [int(x) for x in line.strip().split(' ')]
    dst = nums[1]
    src = nums[0]
    rlen = nums[2]
    return (range(dst, dst+rlen), src-dst)

def readMap(inputLines: 'list[str]'):
    rangeMap: 'list[tuple[range, int]]' = []
    idx = 1
    while (idx < len(inputLines)) and inputLines[idx] != '\n':
        rangeMap.append(makeRangeEntry(inputLines[idx]))
        idx += 1
    return rangeMap, inputLines[idx+1:]