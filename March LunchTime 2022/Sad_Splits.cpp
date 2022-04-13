#include<bits/stdc++.h>
using namespace std;

int  main() 
{
    int test;
    cin>>test;
    while(test--)
    {
        int i=0, j, n;
        string s;
        cin>>s;
        int even=0, odd=0;
        while(s[i])
        { 
        if((s[i]-'0')%2==0) 
        even++;
        else 
        odd++;
    i++;
  }

  
  if(((s[s.size()-1])-'0')&1)
  {
      if(odd>=2)
     cout << "YES\n";
      else cout << "NO\n";
  }
  else{
    if(even>=2)
    cout << "YES\n";
    else
    cout << "NO\n";
  }

}

    return 0;
}
