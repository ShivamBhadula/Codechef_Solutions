try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b,c=map(int,input().split())
            if a>b+c or b>a+c or c>a+b:
                print("YES")
            else:
                print("NO")
except:
    pass