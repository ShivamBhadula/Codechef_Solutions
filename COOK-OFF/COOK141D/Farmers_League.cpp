#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int team;
        cin>>team;
        int ans=0;
        if(team%2==0)
        ans=3*team/2;
        else
        ans=3*(team-1)/2;
        cout<<ans<<endl;
    }
    return 0;

}