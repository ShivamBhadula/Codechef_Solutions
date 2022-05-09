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
        map<int,int> um;
        int res=0,maxi=0;

        for(int i=0;i<n;i++)
        {
            int temp;
            cin>>temp;
            um[temp]++;
            if(um[temp]>maxi)
            {
                maxi=um[temp];
                res=temp;
            }
        }
        bool f=true;

        for(auto x:um)
        {
            if(x.second==maxi and x.first!=res)
            {
                f=false;
            }
        }
        if(f==false)
        {
 cout<<"CONFUSED"<<endl;
                
        }
        else
        {
cout<<res<<endl;
        }





    }
    return 0;
}