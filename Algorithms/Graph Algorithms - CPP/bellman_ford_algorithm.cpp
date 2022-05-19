#include <bits/stdc++.h>
using namespace std;

#define INF 2147000000

vector<int> bellmanFordAlgorithm(int start, vector<vector<vector<int>>> edges)
{

  vector<tuple<int, int, int>> edge_list = vector<tuple<int, int, int>>();
  int N = edges.size();
  for (int a = 0; a < N; a++)
  {
    for (auto e : edges[a])
    {
      edge_list.push_back({a, e[0], e[1]});
    }
  }

  vector<int> distance = vector<int>(N, INF);
  distance[start] = 0;
  for (int i = 0; i < N - 1; i++)
  {
    for (auto e : edge_list)
    {
      int a, b, w;
      tie(a, b, w) = e;
      distance[b] = min(distance[b], distance[a] + w);
    }
  }

  return distance;
}
