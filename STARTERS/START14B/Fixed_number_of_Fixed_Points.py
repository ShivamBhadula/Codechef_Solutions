try:
    def solve(n,k):
        if n==1 and k==0:
            print("-1")
        elif n==1 and k==1:
            print("1")
        elif k==n-1:
            print("-1")
        else:
            result=[] 
            l1=[x for x in range(1,k+1)]
            l2=[x for x in range(k+2,n+1)]
            if k!=n:
                result=l1+l2+[k+1]
            else:
                result=l1+l2
            print(*result)

    if __name__=="__main__":
        for _ in range(int(input())):
            n,k=map(int,input().split())
            solve(n,k)
except:
    pass