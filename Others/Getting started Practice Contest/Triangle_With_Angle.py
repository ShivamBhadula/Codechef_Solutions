try:
    def triangle(a,b,c):
        if a+b+c==180:
            return 'YES'
        return 'NO'

    if __name__=="__main__":
        a,b,c=map(int,input().split())
        if a>0 and b>0 and c>0: 
            print(triangle(a,b,c))
        else:
            print('NO')

except:
    pass