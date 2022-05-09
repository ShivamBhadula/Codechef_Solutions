try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            s=input()
            count=0
            n=s.count('N')
            p=s.count('P')

            count=0
            while p/n!=2:
                p+=1
                n-=1
                count+=1
            print(count)  
                




except:
    pass