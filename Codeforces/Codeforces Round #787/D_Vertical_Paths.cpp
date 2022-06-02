#include "bits/stdc++.h"
using namespace std;

void solve(){
    int n;
    cin >> n;

    int root;
    vector<vector<int>> children(n+1);

    for(int child = 1; child <= n; ++child){
        int parent;
        cin >> parent;
        if(parent == child) {
            root = parent;
        } else {
            children[parent].push_back(child);
        }
    }

    vector<vector<int>> answer;
    vector<int> path;

    function<void(int)> dfs = [&] (int node) {
        path.push_back(node);
        if(children[node].empty()){
            answer.push_back(path);
            path.clear();
        }
        for(int child : children[node]){
            dfs(child);
        }
    };

    dfs(root);

    cout << answer.size() << '\n';
    for(vector<int> path : answer){
        cout << path.size() << '\n';
        for(int node : path){
            cout << node << " ";
        }
        cout << '\n';
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        solve();
    }

}
