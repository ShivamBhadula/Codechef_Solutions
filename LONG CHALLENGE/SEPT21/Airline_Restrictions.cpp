#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ll testcase;
    cin>>testcase;
    while(testcase--)
    {
        ll a,b,c,d,e;
        cin>>a>>b>>c>>d>>e;
        if (((a+b)<=d) &&(c<=e))
        {
            cout<<"YES"<<endl;
        }
        else if ((b+c<=d) && (a<=e))
        {
            cout<<"YES"<<endl;
        }
        else if((a+c<=d) && (b<=e))
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}