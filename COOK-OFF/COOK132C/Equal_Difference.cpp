
//EQDIFFER

#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int a[n];
	    int m=0;
	    map<int,int> mp;
	    
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	        mp[a[i]]++;
	        m=max(m,mp[a[i]]);
            cout<<mp[a[i]]<<endl;
	    }
	    if(n<=2)
	    {
	        cout<<0<<endl;
	        continue;
	    }
	    else if (m==1)
	    {
	        cout<<n-2<<endl;
	        continue;
	    }
	 cout<<n-m<<endl;   
	}
	return 0;
}
