try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            number,k=map(int,input().split())
            l1=[int(x) for x in str(number)]
            l1.sort()
            start=0
            while l1[start]==0:
                l1[start]+=1
                start+=1
                k-=1
            
            


            
except:
    pass