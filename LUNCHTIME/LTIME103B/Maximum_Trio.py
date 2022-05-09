try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            l1.sort()
            j=l1[0]
            i=l1[-1]
            k=l1[-2]
            print((i-j)*k)
except:
    pass