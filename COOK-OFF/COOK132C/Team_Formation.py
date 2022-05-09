
#TEAMFOR

try:
    for _ in range(int(input())):
        length=int(input())
        s1=input()
        s2=input()
        os1=s1.count('1')
        os2=s2.count('1')
        print(min(os1,os2,length//2))
except:
    pass