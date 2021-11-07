try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            x,y,a,b,k=map(int,input().split())
            x+=k*a
            y+=k*b
            if x==y:
                print('SAME PRICE')
            elif x<y:
                print('PETROL')
            else:
                print('DIESEL')
except:
    pass