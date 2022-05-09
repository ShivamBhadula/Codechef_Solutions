try:
    n=int(input())
    for _ in range(n):
        m,ind=input().split(' ')
        lad=0
        for i in range(int(m)):
            yy=input().split(' ')
            if yy[0]=='CONTEST_WON':
                lad+=300
                if int(yy[1])<20:
                    lad+=20-int(yy[1])
            elif yy[0]=='BUG_FOUND':
                lad+=int(yy[1])
            else:
                if yy[0]=='CONTEST_HOSTED':
                    lad+=50
                elif yy[0]=='TOP_CONTRIBUTOR':
                    lad+=300
        if ind=='INDIAN':
            print(lad//200)
        else:
            print(lad//400)

except:
    pass

