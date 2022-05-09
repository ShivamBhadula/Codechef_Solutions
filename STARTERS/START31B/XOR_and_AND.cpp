#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n" 
#define rep(i,a,b) for(auto i = a;i<b;i++)
using namespace std;


void solve(){
    int n;
    cin>>n;  
    unordered_map <int,int> ump;
    int x;
    rep(i,0,n){
        cin>>x;
        int bit = log2(x);
        ump[bit]++;
    }
    int ans =0;
    for(auto num:ump){
        int cur = num.second;
        ans+=(cur*(cur-1))/2;
    }
    cout<<ans<<endl;
}

int32_t main(){
    int T;
    cin>>T;
    for(int i = 1;i<=T;i++){
        solve();
    }
}