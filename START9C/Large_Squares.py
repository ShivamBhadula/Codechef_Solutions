
#XLSQUARE

import math
try:
    for _ in range(int(input())):
        n,a=map(int,input().split())
        if n<4:
            print(a)
        else:
            print(int(math.sqrt(n))*a)
except:
    pass


