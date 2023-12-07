from hand import Hand

INPUTFILENAME = "input"


def main():
    hands = []
    with open(INPUTFILENAME, 'r') as file:
        for line in file:
            hands.append(Hand(line.strip()))
    
    sortedBets = [x.bet for x in sorted(hands)]
    for i in range(len(sortedBets)):
        sortedBets[i] *= i+1
    print(sum(sortedBets))
    


if __name__ == "__main__":
    main()