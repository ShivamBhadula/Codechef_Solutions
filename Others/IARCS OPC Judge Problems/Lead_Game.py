try:
    p1=0
    p2=0
    maxlead=0
    win=0
    for _ in range(int(input())):
        a,b=list(map(int,input().split()))
        p1+=a
        p2+=b
        if p1>p2:
            lead=p1-p2
            if lead>maxlead:
                maxlead=lead
                win=1
        else:
            lead=p2-p1
            if lead>maxlead:
                maxlead=lead
                win=2

    print(win,maxlead)

except:
    pass


