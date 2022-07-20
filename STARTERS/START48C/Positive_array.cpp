#include <bits/stdc++.h> 
using namespace std; 
 
void solve()
    { 
        int n;
        int count = 1, pos = 1; 
        cin>>n;  
        multiset<int> s1; 
        for (int i=0;i<n;i++)
            { 
                int val;
                cin>>val; 
                s1.insert(val); 
            }
        while (s1.size()>0)
        { 
            auto i = s1.lower_bound(pos); 
            if (i!=s1.end())
                { 
                s1.erase(i); 
                pos++; 
                } 
            else
            { 
                pos = 1; 
                count++; 
        } 
    } 
    cout<<count<<endl; 
} 
 
main()
    { 
        int testcase;  
        cin>>testcase; 
        while(testcase--)
            { 
                solve(); 
            } 
    }