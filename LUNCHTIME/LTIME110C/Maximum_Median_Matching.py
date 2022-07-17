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
        l=int(get_input())
        l1=get_list()
        l2=get_list()
        l1.sort()
        l2.sort(reverse=True)
        if l==1:
            return l1[0]+l2[0]
        l4=l1[l//2:]
        # print(l4)
        # print(l5)
        l3=[]

        for i in range(len(l4)):
            val=l4[i]+l2[i]
            l3.append(val)
        # l3=list(set(l3))
        l3.sort()
        # print(l3)
        return l3[0]




    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            ans=solve()
            print(ans)
except:
    pass