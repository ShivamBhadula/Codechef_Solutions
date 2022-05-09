#include<bits/stdc++.h>
using namespace std;


#define gc getchar_unlocked
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define f              first
#define s              second
#define pb              push_back
#define mp              make_pair
#define mt              make_tuple
#define pii             pair<int,int>
#define pll             pair<ll,ll>
#define vi              vector<int>
#define vl             vector<ll>
#define vpii              vector<pii>
#define vpll              vector<pll>
#define mii             map<int,int>
#define mci             map<char,int>
#define msi             map<string,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zerobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define precise(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];
#define all(x) x.begin(), x.end()
#define ini(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define w(t)            ll t; cin>>t; while(t--)
#define w2(t)        ll x; ll t = 0; cin>>x; while( t++ < x )
#define rep(i, n)  for(ll i=0; i<n; i++)
#define iter(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
mt19937  rng(chrono::steady_clock::now().time_since_epoch().count());

#define shuf(x) shuffle(all(x),rng)


const auto start_time = std::chrono::high_resolution_clock::now();



const ll N = 10e6;


int solve(){

    ll n;
    cin>>n;
    string s;
    cin>>s;

    vector<pair<int,int>> vec;

    for(ll i=0; i<n; i++){
        int sz = vec.size();
        int x = sz%2 ? !(s[i] - '0') : s[i] - '0' ; 
        if(x == 1){
            vec.pb({i+1, n-i});
        }
    }
    
    cout<<vec.size()<<endl;
    for(auto x : vec)
    cout<<x.first<<" "<<x.second<<endl;


    return 0;
} 


int32_t main()
{
    //comment it, if using C libaray routines . In order to allow synchronization b/w C and C++.
    ios_base::sync_with_stdio(false);
    
    cin.tie(NULL);cout.tie(NULL);

    w(t){
        solve();
        // cout<<"\n";
    }

    return 0;
}