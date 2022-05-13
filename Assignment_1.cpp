#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int N = 1e5 + 2;
bool vis[N];
vector<int> adj[N];
queue<int> q;

void setVistedtoZero(bool vis[])
{
    for (int i = 0; i <= N; i++)
    {
        vis[i] = false;
    }
}

void DFS(int node)
{
    vis[node] = 1;
    cout << node << " ";

    vector<int>::iterator it;

    for (it = adj[node].begin(); it != adj[node].end(); it++)
    {
        if (vis[*it])
            ;
        else
        {
            DFS(*it);
        }
    }
}

void BFS()
{
    if (q.empty())
        return;
    // deque front and print
    int node = q.front();
    q.pop();
    cout << node << " ";
    vector<int>::iterator it;
    for (it = adj[node].begin(); it != adj[node].end(); it++)
    {
        if (!vis[*it])
        {
            vis[*it] = true;
            q.push(*it);
        }
    }
    BFS();
}

int main()
{
    int n, m;
    cout << "Enter no. of Edges and Vertices: \n";
    cin >> n >> m;

    cout << "Enter starting and ending vertices: \n";
    int x, y;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    int choice;
    do
    {
        cout << "\nCHOICES :-\n1 - DFS\n2 - BFS \n3 - Exit\n";
        cout << "Enter the choice : \n";
        cin >> choice;

        int node;

        switch (choice)
        {
        case 1:
            cout << "Enter the node to start with : \n";
            cin >> node;
            cout << "DFS: \n";
            setVistedtoZero(vis);
            DFS(node);
            break;
        case 2:
            cout << "Enter the node to start with : \n";
            cin >> node;
            q.push(node);
            cout << "BFS: \n";
            setVistedtoZero(vis);
            vis[node] = true;
            BFS();
            break;
        }
    } while (choice != 3);

    return 0;
}