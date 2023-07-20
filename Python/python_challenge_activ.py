
import math


def solution(S, L):
    # Implement your solution here
    nOfCharsInS = dict()
    for i in S:
        if i in nOfCharsInS:
            nOfCharsInS[i] += 1
        else:
            nOfCharsInS[i] = 1

    max = 0

    for i in L:
        nOfCharsInL = dict()
        for j in i:
            if j in nOfCharsInL:
                nOfCharsInL[j] += 1
            else:
                nOfCharsInL[j] = 1

        maxForI = int(len(S) / len(i))
        for j in nOfCharsInL:
            if j in nOfCharsInS:
                if nOfCharsInS[j]/nOfCharsInL[j] < maxForI:
                    maxForI = int(nOfCharsInS[j]/nOfCharsInL[j])
            else:
                maxForI = 0
                break

        if (maxForI > max):
            max = maxForI
    return max

def main():
    print(solution("BILLOBILLOLLOBBI", ["BILL", "BOB"]))

if __name__ == "__main__":
    main()
    
