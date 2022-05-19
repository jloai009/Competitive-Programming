#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
  string name;
  vector<Node *> children;

  Node(string str) { name = str; }

  vector<string> breadthFirstSearch(vector<string> *array)
  {
    queue<Node *> q;
    unordered_set<Node *> visited;
    unordered_map<string, int> distance;
    visited.insert(this);
    distance[this->name] = 0;
    q.push(this);
    while (!q.empty())
    {
      Node *node = q.front();
      q.pop();
      array->push_back(node->name);
      for (Node *child : node->children)
      {
        if (visited.count(child))
        {
          continue;
        }
        visited.insert(child);
        distance[child->name] = distance[node->name] + 1;
        q.push(child);
      }
    }
    return *array;
  }

  Node *addChild(string name)
  {
    Node *child = new Node(name);
    children.push_back(child);
    return this;
  }
};
