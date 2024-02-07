import time

def par_impar(num):
    if num % 2 == 0:
        time.sleep(0.5)
        print("Analisar o número inserido...")
        time.sleep(0.5)
        print(f"\nO numero {num:.0f} é par\n")
    else:
        time.sleep(0.5)
        print("Analisar o número inserido...")
        time.sleep(0.5)
        print(f"\nO numero {num:.0f} é impar\n")