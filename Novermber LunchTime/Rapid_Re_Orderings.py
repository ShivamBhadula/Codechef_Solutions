from statistics import median
import statistics
try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            l2=list(set(l1))
            l2.sort()
            front=0
            back=-1
            start=[]
            end=[]
            test=[]
            while front<len(l2):
                start.append(l2[front])
                test.append(int(statistics.median(start)))
                front+=1
                end.insert(0,l2[back])
                test.append(int(statistics.median(end)))
                back-=1
            if sorted(test)==sorted(l1):
                print(*l2)
            else:
                print("-1")
                







except:
    pass