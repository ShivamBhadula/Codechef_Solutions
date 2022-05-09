try:
    def solve(n):
        val=5
        i=1
        zero=0
        while val**i<=n:
            zero+=n//(val**i)
            i+=1
        print(zero)
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            solve(n)
except:
    pass