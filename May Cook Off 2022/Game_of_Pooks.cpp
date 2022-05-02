#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int n;
        cin>>n;
        if(n<3)
        cout<<1<<endl;
        else if(n==3)
        cout<<2<<endl;
        else
        cout<<n<<endl;
    }
    return 0;
}