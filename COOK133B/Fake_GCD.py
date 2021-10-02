try:
    def solve(n):
        l1=[]
        for i in range(n,0,-1):
            l1.append(i)
        print(*l1)


    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            solve(n)
except:
    pass