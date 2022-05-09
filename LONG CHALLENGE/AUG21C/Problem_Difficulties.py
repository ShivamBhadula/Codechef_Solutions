
#PROBDIFF

try:
    for _ in range(int(input())):
        l1=list(map(int,input().split()))
        l1.sort()
        if l1[0]==l1[1] and l1[2]==l1[3] and l1[1]!=l1[2]:
            print(2)
        else:
            l1=list(set(l1))
            if len(l1)==1:
                print(0)
            elif len(l1)==2:
                print(1)
            elif len(l1)==3:
                print(2)
            elif len(l1)==4:
                print(2)
        

        
except:
    pass