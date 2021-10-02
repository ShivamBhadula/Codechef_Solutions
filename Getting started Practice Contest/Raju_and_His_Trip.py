try:
    def destination(n):
        if n%5==0 or n%6==0:
            return "YES"
        else:
            return "NO"

    if __name__=="__main__":
        print(destination(int(input())))

except:
    pass