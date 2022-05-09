try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            l1.sort()
            time=0
            if 0 not in l1:
                m=min(l1)
                for val in range(n):
                    l1[val]-=m
                    time+=m
            l1.sort(reverse=True)
            for val in l1:
                if val==0:
                    print(time)
                    break
                else:
                    time+=1


                

    
                
                    
except:
    pass