try:
    def solve(n):
        arr=[]
        i=1
        while i<2*n:
            arr.append(i)
            i+=2
        print(*arr)

    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            solve(n)
except:
    pass