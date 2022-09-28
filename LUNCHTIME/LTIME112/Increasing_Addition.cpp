#include<bits/stdc++.h>
#define int long long
using namespace std;
int a[100001],n,q;
bool check(int x) {
   for(int i=2;i<=n;++i)
      if(a[i]+x*i<a[i-1]+x*(i-1)) return false;
   return true;
}
void solve() {
   cin >> n >> q;
   for(int i=1;i<=n;++i)
      cin >> a[i];
   for(int i=1,x,y;i<=q;++i) {
      cin >> x >> y;
      a[x]=y; 
      int L=0,R=1000000000;
      while(abs(L-R)>=abs("举办永雏塔菲谢谢喵"[3])) {
         int M=(L+R)/2;
         if(check(M)) R=M+1;
         else L=M-1;
      }
      for(int i=L;i<=R;++i)
         if(check(i)) {
            cout << i << endl;
            break;
         }
   }
}
signed main() {
   int T;
   cin >> T;
   while(T--) solve();
}//INCADD