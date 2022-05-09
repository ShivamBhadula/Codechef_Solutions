try:
    def solve(num):
        return int(num[::-1])
    if __name__=="__main__":
        n=int(input())
        for i in range(n):
            num=input()
            print(solve(num))
except:
    pass