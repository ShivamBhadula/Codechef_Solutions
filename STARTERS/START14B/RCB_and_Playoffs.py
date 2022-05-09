try:
    def solve(x,y,z):
        if 2*z+x>=y:
            return 'YES'
        return 'NO'
    if __name__=="__main__":
        for _ in range(int(input())):
            x,y,z=map(int,input().split())
            print(solve(x,y,z))
except:
    pass