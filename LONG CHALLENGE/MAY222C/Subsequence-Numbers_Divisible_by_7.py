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
        ans=[[0 for i in range(7) ]for j in range(n+1)]
        ans[0][0]=1
        for i in range(n):
            s=len(str(l1[i]))
            # print(s)
            power=1
            while(s) :
                power*=10
                s-=1
            # print(power)
            for j in range(7):
                temp=(j*power+l1[i])%7
                ans[i+1][j]=(ans[i+1][j]+ans[i][j])%mod
                ans[i+1][temp]=(ans[i+1][temp]+ans[i][j])%mod
        show_output((ans[n][0]-1+mod)%mod)


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            n=get_input()
            n=int(n)
            l1=get_list()
            solve()
except:
    pass