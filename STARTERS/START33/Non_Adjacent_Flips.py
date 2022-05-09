try:
    for _ in range(int(input())):
        n=int(input())
        s=input()
        if '11' in s:
            print(2)
        elif '10' in s:
            print(1)
        elif '01' in s:
            print(1)
        elif '1' in s:
            print(1)
        else:
            print(0)
except:
    pass