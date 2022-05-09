try:
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if a==0 or b==0:
            print(-1)
        else:
            s1="WB"+'W'*(b-1)+'B'*(a-1)
            print(s1)
            for i in range(len(s1)-1):
                print(i+1,i+2)
except:
    pass