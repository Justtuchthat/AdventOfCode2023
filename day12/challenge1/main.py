from hotspring import Hotspring


INPUTFILENAME = "input"


def main():
    hotsprings = []
    with open(INPUTFILENAME, 'r') as input:
        for line in input:
            hotsprings.append(Hotspring(line.strip()))
    totalNumArrangements = 0
    for hotspring in hotsprings:
        totalNumArrangements += hotspring.getNumArrangements()
    print(totalNumArrangements)


if __name__ == "__main__":
    main()