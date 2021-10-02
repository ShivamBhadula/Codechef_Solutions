try:
    def odd(left,right):
        l1=[]
        for i in range(left,right+1):
            if i%2!=0:
                l1.append(i)
        print(*l1)

    if __name__=='__main__':
        left,right=map(int,input().split())
        odd(left,right)

except:
    pass