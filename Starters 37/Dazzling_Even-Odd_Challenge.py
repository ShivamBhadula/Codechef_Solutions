try:
    for _ in range(int(input())):
        n=int(input())
        l1=list(map(int,input().split()))
        a=sum(l1)*2
        if a%n==0 and (a//n)%2==1:
            print("Yes")
        else:
            print("No")
except:
    pass