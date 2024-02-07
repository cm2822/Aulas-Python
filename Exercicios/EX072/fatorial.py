def factorial(num):
    c = num
    f = 1
    print(f"Fatorial: {num:.0f}! = ", end="")
    while c > 0:
        print(f"{c:.0f}", end="")
        print(" x " if c > 1 else " = ", end="")
        f *= c
        c -= 1
    print(f"{f:.0f}")