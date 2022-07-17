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
        s1=get_input()
        i=0
        vowel={'a','e','i','o','u'}
        while i+3<l:
            if s1[i]  not in vowel and s1[i+1]  not in vowel and s1[i+2]  not in vowel and s1[i+3] not in vowel:
                return 'NO'
            # print(s1[i])
            i+=1
        return 'YES'


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            ans=solve()
            show_output(ans)
except:
    pass