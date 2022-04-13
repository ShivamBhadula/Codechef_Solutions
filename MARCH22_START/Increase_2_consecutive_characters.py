try:
    for _ in range(int(input())):
        l,q=map(int,input().split())
        str1=input()
        str2=input()
        for i in range(q):
            l,r=map(int,input().split())
            s1=str1[l-1:r]
            s2=str2[l-1:r]
            l1=[]
            for i in range(len(s1)):
                val=(abs(ord(s1[i])-ord(s2[i])))
                if val==25:
                    val=1
                
                l1.append(val)
            # j=0
            # flag="green"
            # while j+1<len(l1):
            #     if l1[j]==0:
            #         j+=1
            #         continue
            #     if l1[j]==l1[j+1]:
            #         j+=2
            #     else:
            #         flag="red"
            #         break
            # if j+1==len(l1) and l1[-1]!=0:
            #     flag="red"
            # if flag=="red":
            #     print("No")
            # else:
            #     print("Yes")
                    


            

except:
    pass