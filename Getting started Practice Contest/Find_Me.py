try:
    def find(l1,k):
        if k in l1:
            return 1
        else:
            return -1

    if __name__=='__main__':
        n,k=map(int,input().split())
        l1=list(map(int,input().split()))
        print(find(l1,k))

except:
    pass