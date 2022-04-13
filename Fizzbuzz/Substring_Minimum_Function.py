try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n,m=map(int,input().split())
            x=n-m
            if x<=m+1:
                print(x)
            else:
                y=x//m+1
                z=x%(m+1)
                yc=(m+1)-z
                xc=(y+1)
            
                # print(sum)

except:
    pass