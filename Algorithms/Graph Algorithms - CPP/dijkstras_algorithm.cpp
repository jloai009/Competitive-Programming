#include <bits/stdc++.h>
using namespace std;

#define INF 2140000000

vector<int> dijkstrasAlgorithm(int start, vector<vector<vector<int>>> edges)
{
  int N = edges.size();
  priority_queue<pair<int, int>> q = priority_queue<pair<int, int>>();
  vector<int> distance = vector<int>(N, INF);
  vector<bool> processed = vector<bool>(N, false);
  distance[start] = 0;
  q.push({0, start});
  while (!q.empty())
  {
    int a = q.top().second;
    q.pop();
    if (processed[a])
      continue;
    processed[a] = true;
    for (auto u : edges[a])
    {
      int b = u[0], w = u[1];
      if (distance[a] + w < distance[b])
      {
        distance[b] = distance[a] + w;
        q.push({-distance[b], b});
      }
    }
  }
  for (int i = 0; i < N; i++)
  {
    if (distance[i] == INF)
    {
      distance[i] = -1;
    }
  }

  return distance;
}
