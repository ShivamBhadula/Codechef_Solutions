try:
    def solve(*args):
        salary=0
        streak=0
        max_streak=0
        for val in args[2]:
            if val=='1':
                salary+=args[0]
                streak+=1
            else:
                streak=0
            max_streak=max(max_streak,streak)
            
        salary+=max_streak*args[1]
        return salary
    if __name__=="__main__":
        for _ in range(int(input())):
            per_day,bonus=map(int,input().split())
            days=input()
            print(solve(per_day,bonus,days))
except:
    pass