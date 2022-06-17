from math import gcd,sqrt
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
    def printDivisors(n) :
        l=[]
        i = 1
        while i <= sqrt(n) :
            if (n % i==0):
                if(n/i==i):
                    l.append(i)
                    l.append(n-i)
                else:
                    l.append(i)
                    l.append(n-i)
                    l.append(n//i)
                    l.append(n-n//i)
            i = i + 1
        l1=[i for i in l if i!=n]
        l1=[i for i in l1 if i!=0]	
        return len(list(set(l1)))
        

    def solve():
        n=get_input()
        n=int(n)
        ans=printDivisors(n)
        show_output(ans)
        

        


    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass