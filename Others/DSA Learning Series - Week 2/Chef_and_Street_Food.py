try:
    def solve(stores,people,price):
        #print(*stores,*people,*price)
        max_profit=0
        for i in range(len(stores)):
            profit=people[i]//(stores[i]+1)*price[i]
            max_profit=max(max_profit,profit)
        print(max_profit)
    if __name__=="__main__":
        for _ in range(int(input())):
            food_types=int(input())
            stores=[0]*food_types
            people=[0]*food_types
            price=[0]*food_types
            for i in range(food_types):
                stores[i],people[i],price[i]=map(int,input().split())
            solve(stores,people,price)

except:
    pass