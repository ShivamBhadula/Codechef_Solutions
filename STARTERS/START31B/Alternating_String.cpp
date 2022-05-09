#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int len=0;
        cin>>len;
        string s;
        cin>>s;
        int zero=0,one=0;
        for(int i=0;i<len;i++)
        {
            if(s[i]=='0')
            zero++;
            else
            one++;
        }
        if(zero==0 || one==0)
        cout<<1<<endl;
        else if (2*min(zero,one)==len)
        {
            cout<<2*min(zero,one)<<endl;
        }
        else
        {
            cout<<2*min(zero,one)+1<<endl;
        }
    }
    return 0;
}