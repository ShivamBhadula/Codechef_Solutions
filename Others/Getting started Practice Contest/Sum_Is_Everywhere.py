try:
    def sum(n):
        even=0
        odd=0
        for i in range(2*n+1):
            if i%2==0:
                even+=i
            else:
                odd+=i
        return odd,even

    if __name__=="__main__":
        n=int(input())
        print(*sum(n))

except:
    pass