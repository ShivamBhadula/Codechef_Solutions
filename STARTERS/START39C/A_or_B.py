from sys import stdin, stdout
from collections import deque,Counter,OrderedDict,defaultdict,ChainMap,namedtuple
from itertools import permutations,combinations
import heapq
from bisect import bisect_left,bisect_right


def get_abcd(): return map(int, stdin.readline().strip().split())
def get_input(): return stdin.readline().strip()
def get_list(): return list(map(int, stdin.readline().strip().split()))
def get_string(): return stdin.readline().strip()
def get_2str(a): return [stdin.readline().strip() for i in range(a)]
def get_2int(a): return [int(stdin.readline().strip().split()) for i in range(a)]
def show_output(val): stdout.write(str(val)+'\n')


try:


    def solve():
        pass


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            a,b=get_abcd()
            val1=2*a+(4*(a+b))
            val2=((a+b)*2)+(4*b)
            show_output(1500-min(val1,val2))
except:
    pass