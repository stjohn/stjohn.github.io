# CIS 166 Lab 9
# A program to calculate average and maximum line lengths for a file

def main():
    print("This program will calculate the average and maximum line lengths for a file")
    fname = input("Enter file name: ")
    infile = open(fname, "r")
    
    total = 0
    maximum = 0

    lines = infile.readlines()
    n = len(lines)

    for line in lines:
        l = len(line)
        total = total + l
        if l > maximum:
            maximum = l
            average = total / n
    print("max =", maximum, "\taverage line length =", average)

main()
