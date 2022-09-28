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
        if n<=3:
            show_output('-1')
        # elif n==3:
            # show_output('1 3 20')
        elif n==4:
            show_output('2 4 1 3')
        else:
            val=1
            l=[0]*n
            for i in range(0,n,2):
                l[i]=val
                val+=1
            for i in range(1,n,2):
                l[i]=val
                val+=1
            print(*l) 


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass