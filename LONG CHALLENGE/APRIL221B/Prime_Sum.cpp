#include<iostream>
#define ll long long int
#include<algorithm>
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll a,b;
        cin>>a>>b;
        if(a<2 || b<2)
        cout<<-1<<endl;
        else if(__gcd(a,b)==1)
        cout<<1<<endl;
        else
        cout<<0<<endl;
    }
    return 0;
}