#include<iostream>
#define ll long long 
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n ,x;
        cin>>n>>x;
        if(x%n==0)
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
    }
    return 0;
}