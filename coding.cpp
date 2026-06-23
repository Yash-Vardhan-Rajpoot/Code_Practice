#include<bits/stdc++.h>
using namespace std;
string helper(int n,int k,string& str){
    unordered_map<char,int> mp;
    for(char &ch:str) mp[ch]++;
    int count=0;
    for(auto &it:mp){
        int freq=it.second;
        if(freq%2!=0) count+=1;
    }
    int compodd=count-1;
    if(compodd>k) return "NO";
    return "YES";
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        string str;
        cin>>str;
        cout<<helper(n,k,str)<<endl;    
    }
    return 0;
}