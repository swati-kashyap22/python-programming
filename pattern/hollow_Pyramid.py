n=int(input("enter n :"))
for i in range(1,n+1):
    for j in range(n):
        if j==0 or j==n:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()