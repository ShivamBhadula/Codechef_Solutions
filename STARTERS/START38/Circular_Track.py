try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b,m=map(int,input().split())
            ans=min(abs(a-b),abs(m-abs(a-b)))
            print(ans)
except:
    pass