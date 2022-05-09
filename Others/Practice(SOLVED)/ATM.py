
#HS08TEST

x,y=input().split()
x=int(x)
y=float(y)
if (x%5) != 0:
    print("{:.2f}".format(y))
elif (x+0.5) <= y:
    print("{:.2f}".format(y-x-0.5))
else:
    print("{:.2f}".format(y))