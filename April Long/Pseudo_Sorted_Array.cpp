#include<iostream>
#include<vector>
#include<string>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        vector<int> v(n,0);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        ll count=0;
        for(int i=0;i<n-1;i++)
        {
            if(v[i+1]<v[i]){
            swap(v[i+1],v[i]);
            count++;
            }
        }
        if(count==1 || count==0)
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
        // cout<<count<<endl;
    }
    return 0;
}