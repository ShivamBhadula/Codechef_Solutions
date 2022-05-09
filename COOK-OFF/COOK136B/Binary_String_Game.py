try:
    def solve():
        pass
    if __name__=="__main__":
        for _ in range(int(input())):
            l=int(input())
            s=input()
            s1=s[0]
            for c in range(1,l):
                if s[c]!=s[c-1]:
                    s1+=s[c]
            print(s1)
except:
    pass