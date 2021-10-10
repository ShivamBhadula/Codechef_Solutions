try:
    def solve(a,b,c,d):
        if a+b+c<=d:
            return 1
        if a+b<=d:
            return 2
        if a+c<=d:
            return 2
        return 3
        
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b,c,d=map(int,input().split())
            print(solve(a,b,c,d))
except:
    pass