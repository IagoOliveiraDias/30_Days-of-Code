T = int(input("Digite quantas vezes "))

for i in range(T):
    S = input("Digite uma palavra ")
    par = ""
    impar = ""

    for j in range(len(S)):
        if j % 2 == 0:
            par += S[j]
        else:
            impar += S[j]

    print(f"{par} {impar}")
