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
        # print(1)
        n,m=get_abcd()
        # print(n,m)
        l1=get_list()
        l2=get_list()
        for i in range(m):
            l3=[]
            if i%2==0:
                for j in range(len(l1)):
                    if l1[j]%l2[i]!=0:
                        l3.append(l1[j])
            else:
                for k in range(len(l1)):
                    if l1[k]%l2[i]==0:
                        l3.append(l1[k])
            # print(l3)
            l1=l3
        print(*l1)





    if __name__=="__main__":
        # for _ in range(int(stdin.readline())):
        solve()
except:
    pass