#include<bits/stdc++.h>
using namespace std;
vector<int> helper(int a,int b,int c){
    int a1=0,b1=0,c1=0;
    if((a&1)==(b&1)) c1=1;
    if((a&1)==(c&1)) b1=1;
    if((b&1)==(c&1)) a1=1;
    return {a1,b1,c1};

}
    
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        int a,b,c;
        cin>>a>>b>>c;
        vector<int> ans;
        ans=helper(a,b,c);
        for(int i=0;i<ans.size();i++) cout<<ans[i]<<" ";
        cout<<endl;
    }
    return 0;
}