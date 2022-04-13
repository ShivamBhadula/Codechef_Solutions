try:
    for _ in range(int(input())):
        l=int(input())
        l1=list(map(int,input().split()))
        odd=[]
        even=[]
        for val in l1:
            if val%2==0:
                even.append(val)
            else:
                odd.append(val)
        if odd<2:
            print('-1')
        else:
            
except:
    pass