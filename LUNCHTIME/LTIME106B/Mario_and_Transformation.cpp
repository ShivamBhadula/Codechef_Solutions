#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        if(n%3==0)
        cout<<"NORMAL"<<endl;

        else if(n%3==1)
        cout<<"HUGE"<<endl;

        else if(n%3==2)
        cout<<"SMALL"<<endl;
    }
    return 0;
}