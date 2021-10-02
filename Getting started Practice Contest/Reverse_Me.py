try:
    def reverse(l1):
        l1.reverse()
        print(*l1)
    
    if __name__=="__main__":
        n=int(input())
        l1=list(map(int,input().split()))
        reverse(l1)

except:
    pass