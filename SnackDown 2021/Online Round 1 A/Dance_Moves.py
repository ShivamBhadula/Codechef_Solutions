try:
    def solve(x,y):
        if y>x:
            if (y-x)%2==0:
                print((y-x)//2)
            else:
                print((y-x)//2+2)
        elif x>y:
            print(abs(y-x))
        else:
            print(0)
    if __name__=="__main__":
        for _ in range(int(input())):
            x,y=map(int,input().split())
            solve(x,y)
except:
    pass
