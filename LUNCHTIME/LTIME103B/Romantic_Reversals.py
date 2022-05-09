try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n,k=map(int,input().split())
            s1=input()
            s=''
            l1=[0]*n
            k1=k
            flag=True
            for ind in range(k):
                if k1>0 and flag==True:
                    l1[k1-1]=s1[ind]
                    k1-=2
                elif k1==-1 and flag==True:
                    k1=2
                    flag=False
                elif k1==0 and flag==True:
                    k1=1
                    flag=False
                if k1>0 and flag==False:
                    l1[k1-1]=s1[ind]
                    k1+=2
            for val in l1:
                if val==0:
                    break
                s+=str(val)
            if k!=n:
                s+=s1[k:]
            print(s)

            


except:
    pass