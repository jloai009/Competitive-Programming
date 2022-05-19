// CodeChef MINBLOCK Minimize Blocked Roads
// https://www.codechef.com/problems/MINBLOCK

#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> edges;
vector<int> cities_saved;

int dfs(int node, int parent, int blocked) {
    int descendants = 0;

    for(auto edge: edges[node]) {
        int child = edge.first;
        int blockable = edge.second;
        if(child == parent) {
            continue;
        }

        int nodes_in_path = dfs(child, node, blocked or blockable);
        descendants += nodes_in_path;

        if(!blocked and blockable){
            cities_saved.push_back(nodes_in_path);
        }
    }

    return descendants + 1;
}

void solve() {
    int N, K;
    cin >> N >> K;
    edges = vector<vector<pair<int, int>>>(N+1);
    cities_saved.clear();

    for(int i = 0; i < N-1; ++i) {
        int U, V, X;
        cin >> U >> V >> X;
        edges[U].push_back({V, X});
        edges[V].push_back({U, X});
    }

    dfs(1, -1, 0);
    sort(cities_saved.begin(), cities_saved.end());
    reverse(cities_saved.begin(), cities_saved.end());

    int infected = N;
    int roads_blocked = 0;
    for(int n : cities_saved) {
        if(infected <= K) {
            break;
        }
        infected -= n;
        roads_blocked += 1;
    }

    int ans = infected <= K ? roads_blocked : -1;

    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        solve();
    }
}