from math import log
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

    def msb (n):
        k=int(log(n,2))
        return 1<<k

    def solve():
        a,b,n=get_abcd()
        if a==b:
            show_output(0)
        else:
            val=a^b
            if val<n:
                show_output(1)
            else:
                if msb(val)>=n:
                    show_output(-1)
                else:
                    show_output(2)

        


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass