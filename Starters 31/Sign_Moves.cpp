#include<iostream>
using namespace std;
int main()
{
    long long int test;
    cin>>test;
    while(test--)
    {
        long long int n;
        cin>>n;
    long long int res=0;
        if(n%2==0)
        {
            res=n/2;
        }
        else
        {
            res=(n+1)/2;
            res*=-1;
        }
        cout<<res<<endl;
    }
    return 0;
}