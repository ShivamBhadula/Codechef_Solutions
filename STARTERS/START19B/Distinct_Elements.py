try:
    def solve(s):
        count=0
        for i in range(0,s):
            for j in range(i,s):
                count+=1
        return count


    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            l1=list(set(l1))
            ans=n+solve(len(l1))-len(l1)
            print(ans%(10**9+7))

except:
    pass