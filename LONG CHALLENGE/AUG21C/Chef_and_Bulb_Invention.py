
#CHFINVNT

try:
    def jump(n,p,k):
        days=0
        q = (p % k)-1
        s = ((n - 1) // k) * k
        s=n-1-s
        if (q > s):
            days += (s + 1) * ((n - 1) // k + 1) + (q - s) * ((n - 1) // k)
        else:
            days+=((n - 1) // k + 1) * (q + 1)
        i=q+1
        while(i<=n):
            days+=1
            if i==p:
                return days
            i+=k
        

    

    for _ in range(int(input())):
        n,p,k=map(int,input().split())
        print(jump(n,p,k))
    
        
except:
    pass
        





