try:
    def solve(l1):
        if l1.count(1)==l1.count(2):
            print('DRAW')
        elif l1.count(1)>l1.count(2):
            print('INDIA')
        else:
            print('ENGLAND')
    if __name__=="__main__":
        for _ in range(int(input())):
            l1=list(map(int,input().split()))
            solve(l1)

except:
    pass