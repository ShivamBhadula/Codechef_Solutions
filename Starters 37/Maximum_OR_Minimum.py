try:
    for _ in range(int(input())):
        n=int(input())
        l1=list(map(int,input().split()))
        zero=l1.count(0)
        if(zero<=n//2):
            print(1)
        else:
            print(0)
except:
    pass