try:
    def triangle(a,b,c):
        if a+b<=c or a+c<=b or b+c<=a:
            return "NO"
        return "YES"

    if __name__=="__main__":
        a,b,c=map(int,input().split())
        print(triangle(a,b,c))

except:
    pass