from numpy.core.numeric import Inf


try:
    def solve(l1):
        even=[x for x in l1 if x%2==0]
        min_steps=Inf
        if len(even)==len(l1):
            for i in range(len(even)):
                steps=0
                val=even[i]
                while val%2==0:
                    steps+=1
                    val=val//2
                min_steps=min(steps,min_steps)
            return min_steps
        return 0
                


    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1=list(map(int,input().split()))
            print(solve(l1))
except:
    pass