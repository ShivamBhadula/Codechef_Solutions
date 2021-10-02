try:
    def solve(x,y):
        if (abs(x)+abs(y))%2==0:
            print("YES")
        else:
            print("NO")
    if __name__=="__main__":
        for _ in range(int(input())):
            x,y=map(int,input().split())
            solve(x,y)
except:
    pass