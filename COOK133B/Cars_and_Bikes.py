try:
    def solve(n):
        if n%4==0:
            return 'NO'
        return "YES"
    if __name__=="__main__":
        for _ in range(int(input())):
            print(solve(int(input())))
except:
    pass