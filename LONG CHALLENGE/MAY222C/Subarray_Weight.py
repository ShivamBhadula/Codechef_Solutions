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
        ans=0
        for i in range(n):
            for j in range(i+1,n,1):
                temp=l1[i:j+1]
                ans+=abs(l1.index(max(temp))-l1.index(min(temp)))
        show_output(ans)


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            n=get_input()
            n=int(n)
            l1=get_list()
            solve()
except:
    pass