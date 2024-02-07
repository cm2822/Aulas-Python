import time as t
def tabuada(num):
    for c in range(0, 10):
        t.sleep(0.5)
        print(num, "  x  ", c + 1, " = ", num * (c + 1))
