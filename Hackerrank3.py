# HACKERRANK 3 - DAY 3: INTRO TO CONDITIONAL STATEMENTS

if __name__ == '__main__':
    N = int(input("digite um numero: ").strip())
    if 1 <= N <= 100:
        if N % 2 == 0:
            if 2 <= N <= 5:
                print("Not Weird")
            elif 6 <= N <= 20:
                print("Weird")
            elif N > 20:
                print("Not Weird")
        else:
            print("Weird")
    else:
        print("Digite um numero entre 1 e 100")
