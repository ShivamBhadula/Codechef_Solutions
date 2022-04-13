try:
    for _ in range(int(input())):
            n=int(input())
            a=list(map(int,input().split()))
            b=list(map(int,input().split()))
            ans=False
            for i in range(n-2):
                if a[i]>b[i]:
                    ans=False
                    break
                if a[i]!=b[i]:
                    times=b[i]-a[i]
                    a[i]+=times
                    a[i+1]+=times*2
                    a[i+2]+=times*3
            if a[-1]!=b[-1] or a[-2]!=b[-2] or ans:
                print("NIE")
            else:
                print("TAK") 
    
                                 

except:
    pass