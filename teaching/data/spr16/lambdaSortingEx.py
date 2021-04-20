#Data Science, Lehman College, CUNY, Spring 2016
#lambda functions and sorting examples


anon = lambda x: x+"mouse "
print anon("a ")
print anon( anon("anony") )

add = lambda x,y: x+y
print add("a", "mouse")
print add(3,5)

def cat(s, f):
     return f(s)

print cat("mighty", anon)
print cat("mighty", lambda s: add(s,"mouse"))

print sorted("A man a plan a canal: Panama".split(' '), key=str.lower)

#We'll use 11 = Jack, 12 = Queen, 13 = King, 1 = Ace, and
#    C = clubs, D = diamonds, H = hearts, and S = spades
cards = [(10, 'H'), (12, 'C'), (2, 'D'), (4, 'H'), (2, 'C'),
         (12, 'S'), (13, 'S'), (1, 'C'), (5, 'D'), (7, 'H'),
         (8,'D'), (7,'C'), (9,'D')]

print "Original list:", cards
print "Plain sorted:", sorted(cards)
print "Sorted by last value:", sorted(cards, key = lambda card: card[-1])
print "Sorted by suit, then rank:", sorted(cards, key = lambda card: (card[1],card[0]))

print "Original list:", cards
cards.sort()
print "After sort():", cards
cards.sort(key= lambda card: -card[0])
print "Odd sort():", cards
