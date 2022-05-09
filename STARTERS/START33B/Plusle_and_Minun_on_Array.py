try:
    for _ in range(int(input())):
        n=int(input())
        l1=list(map(int,input().split()))
        even=[]
        odd=[]
        for i in range(n):
            if l1[i]<0:
                l1[i]=l1[i]*-1
            if i%2==0: 
                even.append(l1[i])
            else:
                odd.append(l1[i])
        ans1=sum(even)-min(even)+max(odd)
        ans2=sum(odd)-max(odd)+min(even)
        ans=max(ans1-ans2,sum(even)-sum(odd))
        print(ans)
except:
    pass