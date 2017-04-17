
def main():
    s = input("Enter file name: ")
    infile = open(s, "r")

    sum = 0

    for line in infile:
        nums = line.split(",")
        for  n in nums:
            sum = sum + eval(n)

    print(sum)


main()
