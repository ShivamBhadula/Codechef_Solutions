try:
    def solve(l1,n):
        max_val=0
        for i in range(n):
            val=l1[i]*(i+1)
            if val>max_val:
                max_val=val
        print(max_val)


    if __name__=="__main__":
        n=int(input())
        l1=[]
        for i in range(n):
            val=int(input())
            l1.append(val)
        l1.sort(reverse=True)
        solve(l1,n)
except:
    pass