#Simple timing program, modified from Python 2.7 documentation

import timeit

def factR(n):
     if n <= 1:
          return 1
     else:
          return n*factR(n-1)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("factR(100)", setup="from __main__ import factR", number=10))

