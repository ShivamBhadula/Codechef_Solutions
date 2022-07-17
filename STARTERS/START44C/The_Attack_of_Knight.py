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
        x1,y1=get_abcd()
        x2,y2=get_abcd()
        val1=[]
        val2=[]
        if x1-1>0:
            if y1+2<9:
                val1.append((x1-1,y1+2))
            if y1-2>0:
                val1.append((x1-1,y1-2))
        if x1+1<9:
            if y1+2<9:
                val1.append((x1+1,y1+2))
            if y1-2>0:
                val1.append((x1+1,y1-2))
        if x1+2<9:
            if y1+1<9:
                val1.append((x1+2,y1+1))
            if y1-1>0:
                val1.append((x1+2,y1-1))
        if x1-2>0:
            if y1+1<9:
                val1.append((x1-2,y1+1))
            if y1-1>0:
                val1.append((x1-2,y1-1))

        if x2-1>0:
            if y2+2<9:
                val2.append((x2-1,y2+2))
            if y2-2>0:
                val2.append((x2-1,y2-2))
        if x2+1<9:
            if y2+2<9:
                val2.append((x2+1,y2+2))
            if y2-2>0:
                val2.append((x2+1,y2-2))
        if x2+2<9:
            if y2+1<9:
                val2.append((x2+2,y2+1))
            if y2-1>0:
                val2.append((x2+2,y2-1))
        if x2-2>0:
            if y2+1<9:
                val2.append((x2-2,y2+1))
            if y2-1>0:
                val2.append((x2-2,y2-1))

        v1=set(val1)
        v2=set(val2)

        if v1 & v2:
            show_output('YES')
        else:
            show_output('NO')




    if __name__=="__main__":
        for _ in range(int(stdin.readline())):
            solve()
except:
    pass