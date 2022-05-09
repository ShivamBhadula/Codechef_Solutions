import numpy as np
try:
    for _ in range(int(input())):
        n=int(input())
        l1=list(map(int,input().split()))
        l1.sort()
        l2=np.array(l1)
        med=int(np.median(l2))       
        mea=int(np.mean(l2))
        ans=0
        print(ans,med,mea)
        # while med!=mea:
        #     ans+=1
        #     if ans%2==0:
        #         l2[0]+=1
        #     else:
        #         l2[-1]+=1
        #     med=int(np.median(l2))
        #     mea=int(np.mean(l2))
        #     l2.sort()
        # print(ans)              

except:
    pass