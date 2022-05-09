try:
    def pattern(n):
        for i in range(1,n+1):
            print(' '*(n-i-1),'*'*i)
    
    if __name__=='__main__':
        n=int(input())
        pattern(n)

except:
    pass