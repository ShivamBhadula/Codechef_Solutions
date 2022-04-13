#include<iostream>
using namespace std;
int main()
{
    long test;
    cin>>test;
    while(test--)
    {
        long long n;
        cin>>n;
        if(n%4==3 || n%4==2)
        cout<<3<<endl;
        else if(n%4==0)
        cout<<n+3<<endl;
        else if(n%4==1)
        cout<<n<<endl;
    }
    return 0;
}