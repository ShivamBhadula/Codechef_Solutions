#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int dis,cl;
        cin>>dis>>cl;
        if(dis*100<10*cl)
        cout<<"Disposable"<<endl;
        else
        cout<<"Cloth"<<endl;
    }
    return 0;
}