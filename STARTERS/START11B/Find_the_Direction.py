try:
    for _ in range(int(input())):
        n=int(input())
        if n%4==0:
            print('North')
        elif n%4==1:
            print('East')
        elif n%4==3:
            print('West')
        else:
            print('South')

except:
    pass