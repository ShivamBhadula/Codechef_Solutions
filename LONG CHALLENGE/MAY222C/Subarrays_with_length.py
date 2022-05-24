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


try:


    def solve():
        ans=0
        d=defaultdict(int)
        for i in range(n):
            winsize=l1[i]
            start=i-winsize+1 if i-winsize>=0 else 0
            if (l1[i]) in d and d[(l1[i])]>=start:
                start=d[l1[i]]+1
            end=n-1 if start+winsize-1>=n else start+winsize-1
            if end-start+1!=winsize or start>end:
                continue
            ans+=min(i-start+1,n-end)
            d[(l1[i])]=i
        print(ans)


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            n=get_input()
            n=int(n)
            l1=get_list()
            solve()
except:
    pass