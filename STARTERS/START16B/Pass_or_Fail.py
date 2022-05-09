try:
    def solve(*args):
        number=(args[1]*3)-(args[0]-args[1])
        if number>=args[2]:
            return "PASS"
        return "FAIL"
    if __name__=="__main__":
        for _ in range(int(input())):
            questions,correct,marks=map(int,input().split())
            print(solve(questions,correct,marks))
except:
    pass