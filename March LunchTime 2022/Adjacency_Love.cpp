#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    int t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        vector<ll>odd;
        vector<ll>even;
        for(ll i=0;i<n;i++){
            ll y;
            cin>>y;
            if(y&1){
                odd.push_back(y);
            }
            else{
                even.push_back(y);
            }           
               
        }
        if(odd.size()==n && (n&1)){
            cout<<-1<<endl;
        }
        else if(odd.size()==1 && even.size()>0){
            cout<<-1<<endl;           
        }
        else if(odd.size()==1 && even.size()==0){
            cout<<odd[0]<<endl;       
        }                 
        else if(odd.size()>=2){
            if (odd.size()&1){
                cout<<odd[0]<<" ";
                for(ll i=0;i<even.size();i++){
                    cout<<even[i]<<" ";
                } 
                for(ll i=1;i<odd.size();i++){
                    cout<<odd[i]<<" ";
                }
                cout<<endl;
            }
            else {
                for(ll i=0;i<even.size();i++){
                    cout<<even[i]<<" ";
                } 
                for(ll i=0;i<odd.size();i++){
                    cout<<odd[i]<<" ";
                }
                cout<<endl;
            }     
                 
        }
        else{
            cout<<-1<<endl;
        }
    }
 return 0;
}