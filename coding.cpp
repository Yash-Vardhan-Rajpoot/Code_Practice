#include<bits/stdc++.h>
using namespace std;
void solve(){
    int n;
    cin>>n;
    string str;
    cin>>str;
    map<char,int> mp;
    for(char &ch:str) mp[ch]++;
    char chmax,chmin;
    int maxi=INT_MIN;
    int mini=INT_MAX;
    for(auto &it:mp){
        if(it.second>maxi){
            maxi=it.second;
            chmax=it.first;
        }
        if(it.second<=mini){
            mini=it.second;
            chmin=it.first;
        }
    }
    if(mini==maxi){
        for(int i=0;i<n-1;i++){
            if(str[i]!=str[i+1]){
                str[i+1]=str[i];
                break;
            }
        }
    }else{
        for(int i=0;i<n;i++){
            if(mp[str[i]]==mini) {
                str[i]=chmax;
                break;
            }
        }
    }
    cout<<str<<endl;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}