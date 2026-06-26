#include<bits/stdc++.h>
using namespace std;
pair<int,int> helper(int n,int h1,int m1,vector<pair<int,int>>&t){
    bool check=false;
    for(auto &p:t){
        int h2=p.first;
        int m2=p.second;
        if(h1==h2 and m1==m2){
            check=true;
            break;
        }
    }
    if(check) return {0,0};
    else{
        vector<pair<int,int>> p;
        for(auto &pa:t){
            int h2=pa.first;
            int m2=pa.second;
            if(h1<h2){
                if(m2>=m1) p.push_back({h2-h1,m2-m1});
                else p.push_back({h2-h1-1,m2-m1+60});
            }
            else if(h1==h2){
                if(m2>m1) p.push_back({h2-h1,m2-m1});
                else{
                    int addh=0,addm=0;
                    if(m2==0) addh=24-h1;
                    else{
                        addh=23-h1;
                        addm=60-m1;
                    }
                    addm+=m2;
                    if(addm>=60){
                        addh+=1;
                        addm%=60;
                    }
                    p.push_back({addh+h2,addm});
                }
            }
            else{
                int addh=0,addm=0;
                if(h2!=0 and m2==0) addh=24-h1;
                else{
                    addh=23-h1;
                    addm=60-m1;
                }
                addm+=m2;
                if(addm>=60){
                    addh+=1;
                    addm%=60;
                }
                p.push_back({addh+h2,addm});
            }
        }
        sort(begin(p),end(p));
        return {p[0].first,p[0].second};
    }
}
    
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        int n,h,m;
        cin>>n>>h>>m;
        vector<pair<int,int>>t;
        for(int i=0;i<n;i++){
            int h1,m1;
            cin>>h1>>m1;
            t.push_back({h1,m1});
        }
        pair<int,int> ans=helper(n,h,m,t);
        cout<<ans.first<<" "<<ans.second<<endl;
    }
    return 0;
}