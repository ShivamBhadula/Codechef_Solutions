try:
    for _ in range(int(input())):
        n,x,y=map(int,input().split())
        print((x-1)+(n-x)+(y-1)+(n-y)+(min(x-1,n-y))+(min(n-x,n-y))+min((y-1,n-x))+(min(y-1,x-1)))
except:
    pass