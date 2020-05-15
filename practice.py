a=int(input())
b=1

for i in range(a):
    for j in range(1,101):
        if j==round(100/((2 ** i)+1)*b) and j<100:
            print("X", end='')
            b=b+1
        else:
            print("-", end='')

    b=1
    print("\n")