#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll test;
    cin>>test;
    while(test--)
    {
        ll n,x,y;
        cin>>n>>x>>y;
        ll top=x-1;
        ll down=n-x;
        ll left=y-1;
        ll right=n-y;
        ll d1=min(top,right);
        ll d2=min(right,down);
        ll d3=min(down,left);
        ll d4=min(left,top);
        cout<<top+down+left+right+d1+d2+d3+d4<<endl;
    }
    return 0;
}