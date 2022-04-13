try:
    def solve(l1,l2,n,a,b):
        l1.sort()
        l2.sort()
        g=1
        max_g=1
        lg=[]
        time=l1[0]
        lt=[]
        i=1
        j=0
        while i<n and j<n:
            if l1[i]<=l2[j]:
                g=g+1
                if g>max_g:
                    max_g=g
                    lg.append(max_g)
                    lt.append(l1[i])
                i+=1
            else:
                g=g-1
                j+=1
        val=0
        for i in range(a,b+1):
            val+=i
        for k in range(len(lt)):
            if lt[k]>val:
                lt.remove(lt[k])
                lg.remove(lg[k])
        if len(lt)>0:
            print(max(lg))
        else:
            print(0)
        
    if __name__=="__main__":
        for _ in range(int(input())):
            n,a,b=map(int,input().split())
            l1=[]
            l2=[]
            for i in range(n):
                x,y=map(int,input().split())
                l1.append(x)
                l2.append(y)
            solve(l1,l2,n,a,b)
except:
    pass