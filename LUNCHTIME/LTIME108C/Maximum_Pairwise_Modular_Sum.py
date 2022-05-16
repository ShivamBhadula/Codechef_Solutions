from sys import stdin, stdout
from collections import deque,Counter,OrderedDict,defaultdict,ChainMap,namedtuple
from itertools import permutations,combinations
import heapq
from bisect import bisect_left,bisect_right


def get_abcd(): return map(int, stdin.readline().strip().split())
def get_str(): return stdin.readline().strip()
def get_list(): return list(map(int, stdin.readline().strip().split()))
def get_string(): return stdin.readline().strip()
def get_2str(a): return [stdin.readline().strip() for i in range(a)]
def get_2int(a): return [int(stdin.readline().strip().split()) for i in range(a)]
def show_output(val): stdout.write(str(val)+'\n')


try:


    def solve():
        l1.sort(reverse=True)
        val=0
        ans=0
        for i in range(len(l1)):
            for j in range(len(l1)):
                val1=l1[i]+l1[j]+((l1[i]-l1[j])%m)
                val2=l1[i]+l1[j]+((l1[j]-l1[i])%m)
                val=max(val1,val)
                if val<ans:
                    return ans
                ans=max(ans,val)
        return ans
        



    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            n,m=get_abcd()
            l1=get_list()
            l1=list(set(l1))
            res=solve()
            show_output(res)
except:
    pass