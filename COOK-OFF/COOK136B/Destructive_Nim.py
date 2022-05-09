try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            if n%2==0 and sum(l1)%2==0:
                print("Ashish")
            elif n%2==1 and sum(l1)%2==1:
                print("Ashish")
            else:
                print("Utkarsh")
except:
    pass