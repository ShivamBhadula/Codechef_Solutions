from sys import stdin, stdout,maxsize
from collections import deque,Counter,OrderedDict,defaultdict,ChainMap,namedtuple
from itertools import permutations,combinations
import heapq
from bisect import bisect_left,bisect_right


def get_abcd(): return map(int, stdin.readline().strip().split())
def get_str(): return stdin.readline().strip()
def get_list(): return list(map(int, stdin.readline().strip().split()))
def get_string(): return stdin.readline().strip()
def get_2str(a): return [stdin.readline().strip() for i in range(a)]
def get_2int(a): return [int(stdin.readline().strip().split()) for i in range(a)]
def show_output(val): stdout.write(str(val)+'\n')


try:


    def solve():
        if y*z+w==x:
            show_output('filled')
        elif y*z+w>x:
            show_output('overFlow')
        else:
            show_output('Unfilled')


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            w,x,y,z=get_abcd()
            solve()
except:
    pass