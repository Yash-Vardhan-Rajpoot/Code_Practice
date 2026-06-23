#include<bits/stdc++.h>
using namespace std;
string helper(string& str){
    int n=str.size();
    set<char> _set;
    for(int i=0;i<n;i++) _set.insert(str[i]);
    char ch1,ch2;
    for(auto &it:_set){
        for(int i=0;i<n;i++){
            if(it==str[i]) break;
            if(str[i]>it){
                ch1=it;
                ch2=str[i];
                break;
            }
        }
    }
    string ans="";
    for(int i=0;i<n;i++){
        if(str[i]==ch2) ans+=ch1;
        else if(str[i]==ch1) ans+=ch2;
        else ans+=str[i];
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string str;
    cin>>str;
    cout<<helper(str)<<endl;
    return 0;
}