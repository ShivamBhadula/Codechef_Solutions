#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int> v(n);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        vector<int> b(32);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<32;j++)
            {
                b[j]+=(v[i]&(1<<j))>0;
            }
        }
        int ans=0;
        for(int i=0;i<32;i++)
        {
            if(b[i]>=2)
            {
                ans |=(1<<i);
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}