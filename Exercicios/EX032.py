"""# Ex 032 Sequência de Fibonacci

n = 10
num1 = 0
num2 = 1
num_seg = num2
seq = 1

while seq <= n:
    print(num_seg, end=" ")
    seq += 1
    num1, num2 = num2, num_seg
    num_seg = num1 + num2
print()
"""
