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
        if n<3:
            show_output(2)
            return
        l2=[l1[0]]
        for j in range(1,n):
            if l2[0]!=l1[j]:
                l2.append(l1[j])
                break
        for i in range(j,n):
            if l1[i]!=l2[-1] and l1[i]!=l2[-2]:
                l2.append(l1[i])
        # print(l2)
        show_output(len(l2))


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass