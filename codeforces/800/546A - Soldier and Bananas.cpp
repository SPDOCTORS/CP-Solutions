#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    long k,n,w;
    cin>>k>>n>>w;
    long dollars_need=0;
    for (long i=1 ;i<=w;i++)
    {
        dollars_need+=i*k;
    }
    long mo_short=dollars_need-n;
    if (mo_short>0)
    {
        cout<<mo_short<<"\n";
    }
    else
    {
        cout<<"0\n";
    }
    return 0;
}
        
    