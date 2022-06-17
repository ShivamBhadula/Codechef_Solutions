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

    def palindrome(n,x):
        res=""
        for i in range(x):
            res+=chr(ord('a')+i)
        if n-2*x>0:
            res+=res[-1]*(n-2*x)
        res2=""
        for i in range(n-len(res)):
            res2+=chr(ord('a')+i)
        res+=res2[::-1]
        return res        
        
        


    def solve():
        n,x=get_abcd()
        ans=palindrome(n,x)
        if len(ans)==n and ans==ans[::-1]:
            show_output(ans)
        elif n==1 and x==1:
            show_output('a')
        else:
            show_output(-1)


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass