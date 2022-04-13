try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            n=n-1
            result=[]
            i=1
            while i*i<=n:
                if n%i==0:
                    result.append(i)
                    if n//i!=i:
                        result.append(n//i)
                i+=1
            print(len(result))


except:
    pass