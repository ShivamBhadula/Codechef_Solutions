#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin>>t;
  while(t--)
  {
      int n,k;
      cin>>n>>k;
      priority_queue<int,vector<int>,greater<int> >pq;
      while(n!=0)
      {
          pq.push(n%10);
          n/=10;
      }
    while(k--)
    {
        if(pq.top()==9)
        break;
        else
        {
            int temp=pq.top();
            pq.pop();
            pq.push(temp+1);
        }
    }
    int count=1;
    while(!pq.empty())
    {
        count*=pq.top();
        pq.pop();
    }
    cout<<count<<endl;
  }
}
