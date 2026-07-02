#include<bits/stdc++.h>
using namespace std;
string helper(string &str){
    unordered_map<char,int> mp;
    for(auto &ch:str) mp[ch]++;
    bool check=true;
    int s=0,e=str.size()-1;
    while(s<e){
        if(str[s]==str[e]){
            s++;
            e--;
        }else{
            check=false;
            break;
        }
    }
    if(!check) return str;
    else{
        string ans="";
        if(mp.size()==1) return "-1";
        else{
            for(auto &i:mp){
                char ch=i.first;
                int freq=i.second;
                for(int i=0;i<freq;i++) ans+=ch;
            }
        }
        return ans;
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        string str;
        cin>>str;
        cout<<helper(str)<<endl;
    }
    return 0;
}