#include<iostream>
#include<algorithm>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll x,y;
        cin>>x>>y;
        cout<<min(3*x,2*y)<<endl;
    }
    return 0;
}