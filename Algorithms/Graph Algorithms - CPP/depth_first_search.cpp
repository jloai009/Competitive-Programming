#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
  string name;
  vector<Node *> children;

  Node(string str)
  {
    name = str;
    visited.clear();
  }

  static unordered_set<string> visited;

  vector<string> depthFirstSearch(vector<string> *array)
  {
    if (visited.count(this->name))
    {
      return *array;
    }
    visited.insert(this->name);

    array->push_back(this->name);
    for (Node *node : this->children)
    {
      node->depthFirstSearch(array);
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

unordered_set<string> Node::visited = unordered_set<string>();
