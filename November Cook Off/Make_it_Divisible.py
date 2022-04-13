try:
    def solve(l1,n):
        one=0
        two=0
        for i in range(n):
            val=l1[i]%3
            if val==1:
                one+=1
            elif val==2:
                two+=1
        if one==two:
            print(one)
        else:
            diff=abs(one-two)
            v=min(one,two)
            if diff%3==0:
                if one==0 or two==0:
                    print(int(diff//1.5))
                else:
                    print(v+int(diff//1.5))
            else:
                print(-1)

    if __name__=="__main__":
        for _ in range(int(input())):
            size=int(input())
            l1=list(map(int,input().split()))
            solve(l1,size)
except:
    pass