#EX 022 
i = 0
f = 100
salto = 2

for mj in range(i,f, salto):
    print(mj)

for c in range(i, f):
    if c == 0:
        continue
    elif c % 2 == 0:
        print(c)
