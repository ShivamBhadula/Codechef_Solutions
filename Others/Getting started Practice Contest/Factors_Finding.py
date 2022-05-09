try:
    n=int(input())
    count=0
    l1=[]
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            l1.append(i)
    print(count)
    print(*l1)
except:
    pass