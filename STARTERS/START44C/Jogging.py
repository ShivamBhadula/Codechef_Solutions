from sys import stdin, stdout
from collections import deque,Counter,OrderedDict,defaultdict,ChainMap,namedtuple
from itertools import permutations,combinations
from math import pow
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

    def solve(l1):
        n,k=get_abcd()
        ans=(l1[n-1]*k)%mod
        show_output(ans)
        



    if __name__=="__main__":
        l1=[1]
        for i in range(1000000):
            val=l1[-1]*2
            val%=mod
            l1.append(val)
        for _ in range(int(stdin.readline())):
            solve(l1)
except:
    pass