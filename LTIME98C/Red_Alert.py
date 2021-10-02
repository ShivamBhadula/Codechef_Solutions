

#REDALERT


try:
    for i in range(int(input())):
        days,vapor,danger=map(int,input().split())
        l1=list(map(int,input().split()))
        water=0
        for j in l1:
            if j==0:
                water=water-vapor
            elif j>0 :
                water=water+j
            if water<0:
                water=0
            if water>danger:
                exit
        if water>danger:
            print("YES")
        else:
            print("NO")
            
except:
    pass