#include<iostream>
#include<vector>
#define  ll long long
using namespace std;
int main()
{
    ll test;
    cin>>test;
    while(test--)
    {
        int n,m;
        cin>>n>>m;

        vector<int> life(n,0);
        vector<int> power(m,0);
        vector<int> cap(m,0);
        vector<int> left(n,0);

        for(int i=0;i<n;i++){
        cin>>life[i];
        left[i]=life[i];
        }

        for(int i=0;i<m;i++)
        cin>>power[i];

        for(int i=0;i<m;i++)
        cin>>cap[i];

        
        
        for(int i=0;i<m;i++)
        {
            int c=0;
            for(int j=0;j<n;j++)
            {
                if(c==cap[i])
                break;
                if(left[j]<=0)
                {
                    left[j]=0;
                    continue;
                }
                left[j]-=power[i];
                c++;
                
            }
        }

        for(int i=0;i<n;i++)
        {
            if(left[i]<0)
            left[i]=0;
            cout<<left[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}