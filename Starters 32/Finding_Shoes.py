try:
    for _ in range(int(input())):
        n,m=map(int,input().split())
        right=n
        left=n-m
        if left<0:
            left=0
        print(left+right)
except:
    pass