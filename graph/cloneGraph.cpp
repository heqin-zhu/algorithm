/* mbinary
#########################################################################
# File : cloneGraph.cpp
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-04-16  09:41
# Description:
#########################################################################
*/
class Solution {
public:
    map<Node*,Node*> st;
    Node *cloneGraph(Node *node){
        Node* ret = new Node(node->val,vector<Node*>());
        st[node]=ret;
        for(auto x:node->neighbors){
            auto p = st.find(x);
            if(p==st.end()){
                ret->neighbors.push_back(cloneGraph(x));
            }else ret->neighbors.push_back(p->second);
        }
        return ret;
    }
};
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
