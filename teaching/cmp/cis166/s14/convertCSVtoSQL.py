# Program to convert CSV file of customer data into SQL insert statements

def main():
    #Ask user for input and output file names
    inName = input("Enter input filename: ")
    outName = input("Enter output filename: ")

    #Open files to be used in the program
    infile = open(inName,"r")
    outfile = open(outName,"w")
    
    #For each line,
    for line in infile.readlines():
        #Separate out the first and last names
        #Format the insert string and write it to the file
        last, first = line[:-1].split(',')
        s = "insert into customer (first, last) values ('{0}','{1}')".format(first.lstrip(),last)
        print(s, file = outfile)
        print("\tWrote {0} to {1}.".format(last,outName))
		
    #Close files
    infile.close()
    outfile.close()
	
main()
