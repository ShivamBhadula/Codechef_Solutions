try:
    def solve(l1):
        if sum(l1)>3:
            return "YES"
        return "NO"
    if __name__=="__main__":
        n=int(input())
        for i in range(n):
            l1=list(map(int,input().split()))
            print(solve(l1))
except:
    pass