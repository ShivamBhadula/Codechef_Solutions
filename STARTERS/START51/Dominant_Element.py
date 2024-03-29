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
        n=int(get_input())
        l1=get_list()
        l1=Counter(l1)
        l1=l1.most_common(2)
        first=l1[0][1]
        try:
            second=l1[1][1]
        except:
            second=0
        if first==second:
            show_output('NO')
        else:
            show_output('YES')

    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass