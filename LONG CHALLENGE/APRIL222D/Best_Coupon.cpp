#include<iostream>
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
        cout<<max(int(n/10),100)<<endl;
    }
    return 0;
}