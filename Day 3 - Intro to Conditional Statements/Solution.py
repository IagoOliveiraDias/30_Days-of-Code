if __name__ == '__main__':
    N = int(input().strip())
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
        print("Type a number between 1 and 100")
