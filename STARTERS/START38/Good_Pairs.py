try:
    def solve(a,b,l):
        d={}
        ans=0
        print(ans)
        d[a[0]][b[0]]=1
        print(d)

        # for i in range(l):
        #     if d[a[i]][b[i]]==1:
        #         ans+=1
        #     else:
        #         d[a[i]][b[i]]=1
        return ans
    if __name__=="__main__":
        for _ in range(int(input())):
            l=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            print(solve(a,b,l))
except:
    pass