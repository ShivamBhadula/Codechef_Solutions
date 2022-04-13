#include<iostream>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int m,x;
        cin>>m>>x;
        m--;
        int arr[x];
        arr[0]=1;
        int val;
        for(int i=1;i<x;i++)
        {
            val=(m%(i+1))+1;
            if(arr[i-1]<val)
            arr[i]=arr[i-1];
            else
            arr[i]=arr[i-1]+1;
        }
        for(int i=0;i<x;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
        
    }
    return 0;
}