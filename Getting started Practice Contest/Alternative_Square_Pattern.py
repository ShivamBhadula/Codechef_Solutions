def pattern(n):
    fw=[1,2,3,4,5]
    bk=[10,9,8,7,6]
    for i in range(n):
        if i%2==0:
            print(*fw)
            fw=[x+10 for x in fw]
        else:
            print(*bk)
            bk=[x+10 for x in bk]

if __name__=='__main__':
    val=int(input())
    pattern(val)
