from collections import deque


V = 6

adj = [[] for i in range(V)]

edges = [
    (1, 2),
    (1, 4),
    (2, 3),
    (4,3),
    (2,5),
    (3,5)    
    
]

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)  
print(adj)



def bfs(adj):
    visited = [False] * len(adj)
    ans =[]
    q = deque()
    visited[1] = True
    q.append(1)

    while q:
        node = q.popleft()
        ans.append(node)
        
        for x in adj[node]:
            if not visited[x]:
                visited[x] =True
                q.append(x)
                
    return ans


print(bfs(adj))
            
        
        