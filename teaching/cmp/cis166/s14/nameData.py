#Lab:  calculating popularity of names in SSA data

def main():
    #Set the totals to 0 to start:
    total, numTimes = 0,0

    #Set the max's to 0 to start:
    maxOccur,maxYear = 0,0
    
    fname = input("Please enter the file name: ")
    infile = open(fname, "r")

    #Name we're searching for in the file:
    searchee = input("Please enter the first name: ")



    for l in infile.readlines():
        #The year always occurs in positions [4,8]:
        year = eval(l[4:8])
        
        #Split the rest of the line on the comma:
        w = l[8:].split(",")

        #w has the name, followed by the occurrences:
        name = w[0]
        occur = eval(w[1])

        #Check if the current name is the searchee and update:
        if name == searchee:
            total = total + occur
            numTimes += 1
            if occur > maxOccur:
                maxOccur = occur
                maxYear = year

    #Calculate the average and print out the collected data, nicely formatted:
    average = total/numTimes
    print(searchee, "averaged {0:0.02f} times per year.".format(average))
    print("It was most popular in", maxYear, "occurring", maxOccur, "times.")


main()
