#include<iostream>
#include<string>
#define ll long long 
using namespace std;

void solve(int n,int k)
{
    if(k==1)
    {
        if(n%4==0)
        cout<<"On"<<endl;
        else
        cout<<"Ambiguous"<<endl;
    }
    else
    {
        if(n%4==0)
        cout<<"Off"<<endl;
        else
        cout<<"On"<<endl;
    }
}

int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        solve(n,k);
    }
    return 0;
}