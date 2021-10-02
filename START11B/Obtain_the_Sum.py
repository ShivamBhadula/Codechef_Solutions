try:    
    for _ in range(int(input())):
        n,s=map(int,input().split())
        sum=(n*(n+1))//2
        if sum-s>0 and sum-s<=n:
            print(sum-s)
        else:
            print('-1')
except:
    pass