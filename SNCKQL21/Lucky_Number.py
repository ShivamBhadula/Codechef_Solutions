try:
    def solve(*args):
        if 7 in args:
            print("YES")
        else:
            print("NO")
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b,c=map(int,input().split())
            solve(a,b,c)
except:
    pass