try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            a,b,k=map(int,input().split())
            if abs(a)%abs(k) and abs(b)%abs(k):
                print("NO")
            else:
                print("YES")
except:
    pass