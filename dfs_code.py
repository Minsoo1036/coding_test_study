def dfs(graph, v, visited): #5줄짜리 코드
  visited[v] = True
  print(v, end=" ")

  for k in graph[v]:
    if not visited[k]:
      dfs(graph,k,visited)
      

graph = [ #인접 리스트
  [], #편의상 0인 노드 있다고 가정
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]  
]

visited = [False] * 9
dfs(graph,1,visited)