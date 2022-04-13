try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=[ x for x in range(2,n+1)]
            l1.append(1)
            print(*l1)
except:
    pass