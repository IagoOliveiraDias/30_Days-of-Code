T = int(input())

for i in range(T):
    S = input()
    even = ""
    odd = ""

    for j in range(len(S)):
        if j % 2 == 0:
            even += S[j]
        else:
            odd += S[j]

    print(f"{even} {odd}")
