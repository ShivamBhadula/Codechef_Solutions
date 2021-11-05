try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            x,y=map(int,input().split())
            if (x%2==0 and x!=0) or (x==0 and y%2==0):
                print('YES')
            else:
                print('NO')
except:
    pass