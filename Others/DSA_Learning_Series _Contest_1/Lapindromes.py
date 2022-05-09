from typing import Counter


try:
    def solve(word):
        if len(word)%2==0:
            mid=len(word)//2
            start=word[:mid]
            end=word[mid:]
            if Counter(start)==Counter(end):
                print("YES")
            else:
                print("NO")
        else:
            mid=len(word)//2
            start=word[:mid]
            end=word[mid+1:]
            if Counter(start)==Counter(end):
                print("YES")
            else:
                print("NO")


    if __name__=="__main__":
        n=int(input())
        for i in range(n):
            word=input()
            solve(word)
except:
    pass