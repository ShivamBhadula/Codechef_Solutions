try:
    def triangle(a,b,c):
        if a+b<=c or a+c<=b or b+c<=a:
            return -1
        if a==b==c:
            return 1
        if a==b or b==c or a==c:
            return 2
        return 3

    if __name__=="__main__":
        a,b,c=map(int,input().split())
        print(triangle(a,b,c))

except:
    pass