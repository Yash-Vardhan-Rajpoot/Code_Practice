#include<bits/stdc++.h>
using namespace std;
typedef string str;
typedef vector<int> v;
int helper(v &arr){
    int p1p2p3=arr[0]+arr[1]+arr[2];
    if(p1p2p3%2!=0) return -1;
    if(arr[0]+arr[1]<=arr[2]) return arr[0]+arr[1];
    else return (arr[0]+arr[1]+arr[2])/2;

}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        int p1,p2,p3;
        cin>>p1>>p2>>p3;
        v arr{p1,p2,p3};
        cout<<helper(arr)<<endl;
    }
    return 0;
}