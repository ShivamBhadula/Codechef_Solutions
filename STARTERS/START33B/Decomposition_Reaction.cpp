#include<bits/stdc++.h>
using namespace std;
int main()
{
const long int N = 1000000007;
int solve(){


    ll n, m;
    cin>>n>>m;
    vl q(n);
    for(auto &x : q) cin>>x;

    while(m--){

        ll ci, x;
        
        cin>>ci>>x;

        ll c = q[ci - 1];
        

        vector<int> rct(2*x);
        
        for(auto &a : rct) cin>>a;

        if(c == 0){
            continue;
        }

        q[ci-1] = 0;

        long i = 1;

        while(i < 2*x){

            q[ rct[i] - 1 ] =   (q[ rct[i] - 1 ]  +  (rct[i-1]*c))%N ;
            i += 2;
        } 
          

  

    }

    for( ll x  : q)
    cout<<x%N<<endl;   
  

    return 0;
}
