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
        l1=[0]*(n+1)
        l1[1]=0
        left=0
        right=0

        for i in range(2,n+1,1):
            if i%2==0:
                left-=1
                l1[i]=left
            else:
                right+=1
                l1[i]=right
        for i in range(1,n+1):
            print(l1[i]-left+1,end=" ")

        print()


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass