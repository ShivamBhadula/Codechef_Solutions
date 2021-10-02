#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ll testcase;
    std::cin>>testcase;
    vector<int> a;
    while(testcase--)
    {
        ll n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            ll z;
            cin>>z;
            a.emplace_back(z);
        }
        ll even=0,odd=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]%2==0)
            {
                even++;
            }
            else
            {
                odd++;
            }
        }
        if(n%2==0)
        {
            if (even >= n/2)
            {
                even=n/2;
            }
            else
            {
                odd=n/2;
            }
        }
        else
        {
            if(even>=int(n/2)+1)
            {
                even=int(n/2)+1;
            }
            else
            {
                odd=int(n/2);
            }
        }
        cout<<even+odd<<endl;
    }
    return 0;
}