try:
    def solve(start,size,end):
        if size%2==0:
            print(size//2)
        else:
            if  start==1:
                if end==1:
                    print(size//2)
                else:
                    print((size//2)+1)
            else:
                if end==2:
                    print(size//2)
                else:
                    print(size//2+1)

            
        
    if __name__=="__main__":
        for _ in range(int(input())):
            for i in range(int(input())):
                start,size,end=map(int,input().split())
                solve(start,size,end)

except:
    pass