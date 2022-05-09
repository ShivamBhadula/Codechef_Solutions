#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x,y,z;
        cin>>x>>y>>z;
        int time=y/x;
        if(time>=z)
        cout<<0<<endl;
        else
        cout<<z-time<<endl;
    }
        return 0;
}