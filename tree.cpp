#include <bits/stdc++.h>
using namespace std;
struct node{
    char data;
    node *left,*right;
    node(char val){
        data=val;
        left=right=nullptr;
    }
};
void construct_tree(queue<node*>&q,int level,int curr,char &ans,int &target){
    while(!q.empty() and curr<level){
        int size=q.size();
        int pos=1;
        for(int i=0;i<size;i++){
            node* n=q.front();
            q.pop();
            if(n->data=='E'){
                n->left=new node('E');
                q.push(n->left);
                if(pos==target and curr==(level-1)) ans=n->left->data;
                pos+=1;
                n->right=new node('D');
                q.push(n->right);
                if(pos==target and curr==(level-1)) ans=n->right->data;
                pos+=1;
            }else{
                n->left=new node('D');
                q.push(n->left);
                if(pos==target and curr==(level-1)) ans=n->left->data;
                pos+=1;
                n->right=new node('E');
                q.push(n->right);
                if(pos==target and curr==(level-1)) ans=n->right->data;
                pos+=1;
            }
        }
        curr+=1;
    }
}
void preorder(node* tree){
    if(tree==nullptr) return;
    cout<<tree->data<<" ";
    preorder(tree->left);
    preorder(tree->right);
}
string solve(string &str){

}
int main(){
    int level,target;
    cin>>level>>target;
    node* tree=new node('E');
    queue<node*>q;
    q.push(tree);
    int curr=1;
    char ans;
    construct_tree(q,level,curr,ans,target);
    preorder(tree);
    cout<<endl;
    if(ans=='E') cout<<"Engineer"<<endl;
    else cout<<"Doctor"<<endl;
    return 0;
}