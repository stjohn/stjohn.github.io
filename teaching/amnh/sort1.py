#RGGS, 7 March 2016
#Examples from group work

a = [12,3,1,50,18,6,15,34]
print a, a[::-3]
print max(a), max(a[::-3])

def mystery(a):
     for i in range(1,len(a)):
          if a[i-1] > a[i]:
               a[i-1], a[i] = a[i], a[i-1]


a = [11,34,1,20,18,6,5,3]
print a
mystery(a)
print a
mystery(a)
print a

def mystery2(a,b):
     c = []
     ai = 0
     bi = 0
     while ai < len(a) and bi < len(b):
          if a[ai] < b[bi]:
               c.append(a[ai])
               ai += 1
          else:
               c.append(b[bi])
               bi += 1
     if ai < len(a):
          c = c + a[ai:]
     if bi < len(b):
          c = c + b[bi:]          
     return c
x = [1,3,5,6,7,9]
y = [2,4,8,10,12,15]
z = mystery2(x,y)
print z
