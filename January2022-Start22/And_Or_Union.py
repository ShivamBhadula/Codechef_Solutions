try:
    for _ in range(int(input())):
        n1=int(input())
        l1=list(map(int,input().split()))
        l2=[]
        for i in range(n1):
            for j in range(i+1,n1):
                l2.append(l1[i]&l1[j])
        # print(*l2)
        while len(l2)!=1:
            maximum=max(l2)
            minimum=min(l2)
            l2.remove(maximum)
            l2.remove(minimum)
            l2.append(maximum | minimum)
        print(*l2)

except:
    pass