#input
n=int(input())
for i in range(0, n):
    for j in range(n, i, -1):
        print("1 ", end="")
    print()
