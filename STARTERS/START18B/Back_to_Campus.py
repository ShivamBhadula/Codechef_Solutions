try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            k,n=map(int,input().split())
            if k%n==0:
                print(k//n)
            else:
                print(k//n+1)
except:
    pass