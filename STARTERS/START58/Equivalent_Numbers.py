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
        x,y=get_abcd()
        s1=[x**i for i in range(1,20)]
        s2=[y**i for i in range(1,20)]
        s1=set(s1)
        s2=set(s2)
        if len(s1.intersection(s2))==0:
            show_output('NO')
        else:
            show_output('YES')
        


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass