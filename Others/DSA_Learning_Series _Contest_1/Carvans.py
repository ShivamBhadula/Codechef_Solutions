
try:
    def solve(l1):
        count=1
        for i in range(1,len(l1)):
            if l1[i]<=l1[i-1]:
                count+=1
            else:
                l1[i]=l1[i-1]
        print(count)
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            solve(l1)
except:
    pass