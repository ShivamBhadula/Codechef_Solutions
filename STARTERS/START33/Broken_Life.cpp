#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    while(t--){
    int n,m;cin>>n>>m; 
    bool ok=false;
    string s,t;cin>>s>>t; 
    for(char i='a';i<'f';i++){ 
        int k=0;
        string s1(s.size(),0); 
        for(int j=0;j<s.size();j++){ 
            if(s[j]=='?'){ 
                s1[j]=i; 
            } 
            else{ 
                s1[j]=s[j];  
            } 
            if(s1[j]==t[k] and k < m){
                    k++;
            }   
        }
        if(k!=m){ 
            cout<<s1<<endl; 
            ok=true;
            break; 
        } 
    } 
    if(!ok)
    cout<<-1<<endl; 
    }
    return 0;
}