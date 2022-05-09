#include<iostream>
#include<vector>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        vector<int> v(n,0);
        ll even=0;
        ll odd=0;
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
            if(v[i]%2==0)
            even++;
            else
            odd++;
        }
        ll start=v.front();
        ll end=v.back();
        if(start%2==0 && end%2==0)
        cout<<even-1<<endl;
        else if(start%2==1 && end%2==1)
        cout<<odd-1<<endl;
        else
        {
            
        }
    }
    return  0;
}