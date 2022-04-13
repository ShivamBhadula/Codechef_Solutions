try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            l1.sort()
            print(l1[n//2]-l1[n//2-1])
except:
    pass