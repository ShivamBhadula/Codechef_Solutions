try:
    for _ in range(int(input())):
        x,y,z=map(int,input().split())
        if y<=z:
            print(0)
        else:
            marks=z+1
            total_marks=z*x
            print(total_marks//marks)
except:
    pass
