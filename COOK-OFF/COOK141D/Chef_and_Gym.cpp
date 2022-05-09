#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int x,y,z;
        cin>>x>>y>>z;
        if(z>=x+y)
        cout<<2<<endl;
        else if(z>=x)
        cout<<1<<endl;
        else
        cout<<0<<endl;
    }
    return 0;

}