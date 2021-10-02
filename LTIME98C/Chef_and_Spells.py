
#CHFSPL

try:
    for i in range(int(input())):
        a,b,c=map(int,input().split())
        minimum=min(a,b,c)
        power=(a+b+c)-minimum
        print(power)
except:
    pass