try:
    for _ in range(int(input())):
        n=int(input())
        s=input()
        ans=0
        for i in range(n):
            if(s[i]==s[i+1]):
                ans+=1
                i+=1
            else:
                ans+=1
        print(ans)
                







except:
    pass