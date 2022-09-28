from sys import stdin, stdout
from collections import deque,Counter,OrderedDict,defaultdict,ChainMap,namedtuple
from itertools import permutations,combinations
import heapq
from bisect import bisect_left,bisect_right


def get_abcd(): return map(int, stdin.readline().strip().split())
def get_input(): return stdin.readline().strip()
def get_list(): return list(map(int, stdin.readline().strip().split()))
def get_str(): return list(map(str, stdin.readline().strip().split()))
def get_string(): return stdin.readline().strip()
def get_2str(a): return [stdin.readline().strip() for i in range(a)]
def get_2int(a): return [int(stdin.readline().strip().split()) for i in range(a)]
def show_output(val): stdout.write(str(val)+'\n')


mod=1000000007


try:


    def solve():
        n,x=get_abcd()
        a=get_list()

        dp = [[0 for i in range(2)] for j in range(n+1)]
        
        for i in range(2,n+1):
            dp[i][0]=max(dp[i-1][0]+(a[i-1]^a[i]),dp[i-1][1]+((a[i-1]+x)^a[i]))
            dp[i][1]=max(dp[i-1][0]+(a[i-1]^(a[i]+x)),dp[i-1][1]+((a[i-1]+x)^(a[i]+x)))

        print(max(dp[n][0],dp[n][1]))

    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass