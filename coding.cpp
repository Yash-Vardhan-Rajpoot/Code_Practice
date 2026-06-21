#include<bits/stdc++.h>
using namespace std;
int helper(vector<int>&arr,int n,int x){
    int count=0;
    vector<int> pref(n);
    pref[0]=arr[0];
    for(int i=1;i<n;i++) pref[i]=pref[i-1]+arr[i];
    for(int i=0;i<n;i++){
        int sum=pref[i];
        vector<int> check;
        while(sum>0){
            check.push_back(sum%10);
            sum/=10;
        }
        if(check[0]==x and check[check.size()-1]==x) count+=1;
    }
    int temp=pref[0];
    for(int i=1;i<n;i++){
        for(int j=i;j<n;j++){
            int sum=pref[j]-temp;
            vector<int> check;
            while(sum>0){
                check.push_back(sum%10);
                sum/=10;
            }
            if(check[0]==x and check[check.size()-1]==x) count+=1;
        }
        temp=pref[i];
    }
    return count;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,x;
    cin>>n>>x;
    vector<int> arr(n);
    for(int i=0;i<n;i++) cin>>arr[i];
    cout<<helper(arr,n,x)<<endl;
    return 0;
}