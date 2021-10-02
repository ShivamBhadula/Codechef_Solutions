try:    
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if b<=a:
            print(b)
        else:
            print(a*2-b)
except:
    pass