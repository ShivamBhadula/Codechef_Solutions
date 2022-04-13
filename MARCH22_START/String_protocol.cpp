#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]==s[i+1])
            {
                ans++;
                i++;
            }
            else
            {
                ans++;
            }
        }
        cout<<ans<<endl;


    }
    return 0;
}