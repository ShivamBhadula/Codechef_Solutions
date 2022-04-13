try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            s=input()
            l1=[]
            val=0
            for c in s:
                if c=='(':
                    val+=1
                else:
                    if val!=0:
                        l1.append(val)
                        val=0
            print(min(l1))
except:
    pass