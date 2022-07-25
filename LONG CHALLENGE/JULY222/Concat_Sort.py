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
        l2=sorted(l1)
        l3=[]
        i=0
        j=0
        while i<n and j<n:
            if l1[i]==l2[j]:
                i+=1
                j+=1
            else:
                l3.append(l1[i])
                i+=1
        l4=sorted(l3)
        if l3==l4:
            show_output('YES')
        else:
            show_output('NO')


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass