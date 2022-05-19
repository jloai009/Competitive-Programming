#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> adj_list;
vector<int> state;
vector<int> result;
bool helper(int n);

vector<int> topologicalSort(vector<int> vertices, vector<vector<int>> edges)
{
  result = vector<int>();
  N = vertices.size();
  adj_list = vector<vector<int>>(N + 1);
  state = vector<int>(N + 1, 0);
  for (auto edge : edges)
  {
    adj_list[edge[0]].push_back(edge[1]);
  }

  for (int i : vertices)
  {
    if (state[i] < 2)
    {
      if (!helper(i))
      {
        result.clear();
        break;
      }
    }
  }

  reverse(result.begin(), result.end());
  return result;
}

bool helper(int n)
{
  if (state[n] == 1)
    return false;
  state[n] += 1;
  for (int adj : adj_list[n])
  {
    if (state[adj] < 2)
    {
      if (!helper(adj))
        return false;
    }
  }
  state[n] += 1;
  result.push_back(n);
  return true;
}
