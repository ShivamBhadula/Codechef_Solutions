#include<bits/stdc++.h>
#include<iostream>
int main() 
{
  int testcase;
 std::cin>>testcase;
 while(testcase--)
 {
   int n,a,b;
   std::string str;
   std::cin>>n>>a>>b;
   int district,state,total;
   std::cin>>str;
   district=count(str.begin(),str.end(),'0');
   state=count(str.begin(),str.end(),'1');
   total=(a*district)+(b*state);
   std::cout<<total;
   std::cout<<std::endl;

 }
 return 0;
}