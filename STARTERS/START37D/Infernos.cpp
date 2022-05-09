#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int n,s;
        cin>>n>>s;
        vector<int> v(n,0);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        int multi=*max_element(v.begin(),v.end());
        int single=0;
        for(int i=0;i<n;i++)
        {
            if(v[i]%s==0)
            single+=v[i]/s;
            else
            single+=v[i]/s+1;
        }
        // cout<<single<<" "<<multi<<endl;
        cout<<min(single,multi)<<endl;
    }
    return 0;
}