#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int d;
        int g;
        for(int i=0;i<31;i++)
        {
            int c=(1<<i);
            if(c&n)
            {
                d=i;
                g=c;
            }
        }
        int ans=0;
        int f=1;
        for(int i=0;i<d;i++)
        {
            ans+=(f-1);
            f*=2;
        }
        ans+=(n-g);
        cout<<ans<<endl;
    }
    return 0;
}