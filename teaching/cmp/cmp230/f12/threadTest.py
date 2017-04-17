import time
from threading import Thread
from graphics import *

def myfunc(i,w):
    print ("\nsleeping 2 sec from thread", i)
    time.sleep(2)
    print ("\nfinished sleeping from thread", i)
    w.close()


w = [0]*5
for i in range(5):
    banner = "***" + str(i) + "***"
    w[i] = GraphWin(banner,200,200)    
    t = Thread(target=myfunc, args=(i,w[i]))
    t.start()
