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
        l1=get_string()
        l2=get_string()
        l3=[]
        l4=[]
        l3[:0]=l1
        # print(l3)
        l4[:0]=l2
        for i in range(l):
            l4[i]=int(l4[i])
            l3[i]=int(l3[i])
        if sum(l4)>=1 and sum(l3)==0:
            return 'NO'
        if l3==l4:
            return 'YES'
        even=0
        odd=0
        for i in range(l):
            if i%2==0:
                even+=l4[i]
            else:
                odd+=l4[i]
        
        if even==l//2+1 or odd==l//2+1:
            return 'NO'

        return 'YES'
        



    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            ans=solve()
            show_output(ans)
except:
    pass