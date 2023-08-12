n, m = map(int, input().split())

ice_map = []
for _ in range(n):
  new_line = list(map(int, input().split()))
  ice_map.append(new_line)

def dfs(i,j): # 세로, 가로 순
  if i < 0 or i >= n:
    return 
  if j < 0 or j >= m:
    return

  if ice_map[i][j] == 1: #원래 1이었던 구간
    return False
  else: #새로이 찍은 점 (1이 아니었던 구간)
    ice_map[i][j] = 1
    dfs(i-1,j) #상하좌우 탐색
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    return True #얼음과자 1개 완성

count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) :
      count+=1
  
print(count)