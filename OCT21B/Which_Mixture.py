try:
    def solve(a,b):
        if a>0 and b>0:
            print("Solution")
        elif b==0:
            print("Solid")
        else:
            print("Liquid")
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b=map(int,input().split())
            solve(a,b)
except:
    pass