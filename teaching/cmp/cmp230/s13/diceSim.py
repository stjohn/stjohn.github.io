from random import *

def oneRoll():
    r1 = randrange(8)+1
    r2 = randrange(4)+1
    return(r1+r2)

def main():
    counts = [0]*13

    for i in range(10000):
        counts[oneRoll()] += 1

    for i in range(2,13):
        print(i, ":", counts[i])

main()
