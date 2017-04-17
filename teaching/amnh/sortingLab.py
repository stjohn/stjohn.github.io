


def getInputList():
     """
     No inputs
     Returns the list to sort
     """
     s = raw_input('Please enter a list of numbers, separated by spaces: ')
     a = [int(w) for w in s.split(' ')]
     return a

def sortList(a):
     """
     Takes a list and sorts it in place
     """

def printList(b):
     """
     Prints sorted list.
     No outputs
     """
     print "The sorted list is:"
     print b


def main():
     print "Welcome to the sorting program!"
     #Get list of items to sort.
     a = getInputList()
     #Sort list.
     sortList(a)
     #Print sorted list
     printList(a)
     
if __name__ == "__main__":
     main()
