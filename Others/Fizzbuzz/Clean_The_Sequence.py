try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            length,natural=map(int,input().split())
            arr=list(map(int,input().split()))
            ans=[]
            for i in range(1,natural+1):
                new=[val for val in arr if val!=i]
                count=0
                for j in range(1,len(new)):
                    if new[j]!=new[j-1]:
                        count+=1
                ans.append(count)
            print(*ans)
                    
except:
    pass