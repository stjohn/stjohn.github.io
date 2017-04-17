# wordfreq.py

def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")

###New code between these comments: ###
    
    infile = open(fname,'r',encoding='utf8')

    #Split up the lines to have the number of events each hour,
    #   and put the tweets in text to be processed as before.
    text = ""
    times = {}
    for lines in infile.readlines():
        fields = lines.split("\t")
        text = text + fields[3]
        time = fields[2].split()[1]
        hour = time[0:2]
        times[hour] = times.get(hour,0) + 1
        print(hour, fields[3])	#Print for testing, remove before running final program        

    #Print out when tweets occur:
    items = list(times.items())
    items.sort()
    for item in items:
        #Each item is a list of the key and the associated entry:
        print("At hour", item[0], ", there were", item[1], "tweets.")
        
###New code between these comments: ###  
        
    #Process the text as before:
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words.
    n = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))


if __name__ == '__main__':  main()
