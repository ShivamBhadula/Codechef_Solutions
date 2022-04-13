try:
    for _ in range(int(input())):
        l=int(input())
        l1=list(map(int,input().split()))
        even=0
        odd=0
        for val in l1:
            if val%2==0:
                even+=1
            else:
                odd+=1
        if even==0 or odd==0:
            print(0)
        elif odd%2==1:
            print(even)
        else:
            print(min(odd//2,even))
except:
    pass