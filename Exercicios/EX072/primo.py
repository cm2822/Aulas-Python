import time


def primo(num):
    if num < 2:
        time.sleep(0.5)
        print("Analisar o número inserido...")
        time.sleep(0.5)
        print(f"O número {num:.0f} é primo")
    else:
        num_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                num_primo = False
                break
        if num_primo:
            time.sleep(0.5)
            print("Analisar o número inserido...")
            time.sleep(0.5)
            print(f"O número {num:.0f} é primo.")
        else:
            time.sleep(0.5)
            print("Analisar o número inserido...")
            time.sleep(0.5)
            print(f"O número {num:.0f} não é primo.")
