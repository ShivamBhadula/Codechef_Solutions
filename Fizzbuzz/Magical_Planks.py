try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            length=int(input())
            color=input()
            w1=[]
            b1=[]
            black=0
            white=0
            for col in color:
                if col=='B':
                    if white!=0:
                        w1.append(white)
                    white=0
                    black+=1

                if col=="W":
                    if black!=0:
                        b1.append(black)
                    black=0
                    white+=1
            if black!=0:
                b1.append(black)
            if white!=0:
                w1.append(white)
            print(min(len(w1),len(b1)))
except:
    pass