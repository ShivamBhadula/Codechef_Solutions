try:
    def time(s):
        first=s[0]
        taken=2
        previous=first
        for current in range(1,len(s)):
            if previous=='d' or previous=='f':
                if s[current]=='j' or s[current]=='k':
                    taken+=2
                else:
                    taken+=4
            else:
                if s[current]=='d' or s[current]=='f':
                    taken+=2
                else:
                    taken+=4
            previous=s[current]
            #print(taken,previous)
        return taken

    if __name__=="__main__":
        for _ in range(int(input())):
            n=int(input())
            l1={}
            total=0
            for i in range(n):
                a=input()
                if a in l1:
                    total+=l1[a]//2
                else:
                    total+=time(a)
                    l1[a]=time(a)
            print(total)      

except:
    pass          