#include "bits/stdc++.h"
using namespace std;

void solve(){
    int n;
    cin >> n;

    int root;
    vector<int> parent(n+1);
    vector<bool> is_leaf(n+1, true);
    vector<bool> visited(n+1, false);

    for(int child = 1; child <= n; ++child){
        int curr_parent;
        cin >> curr_parent;
        parent[child] = curr_parent;
        if(curr_parent != child) {
            is_leaf[curr_parent] = false;
        }
    }

    vector<vector<int>> answer;
    vector<int> path;

    for(int node = 1; node <= n; node++){
        if(!is_leaf[node]){
            continue;
        }
        int curr_node = node;
        while(!visited[curr_node]){
            visited[curr_node] = true;
            path.push_back(curr_node);
            curr_node = parent[curr_node];
        }
        reverse(path.begin(), path.end());
        answer.push_back(path);
        path.clear();
    }


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
