try:
    def solve(l1,m):
        l1.sort()
        if m<l1[0] or m>l1[-1]:
            return "NO"
        return "YES"
    if __name__=="__main__":
        for _ in range(int(input())):
            l,m=map(int,input().split())
            l1=list(map(int,input().split()))
            print(solve(l1,m))
except:
    pass