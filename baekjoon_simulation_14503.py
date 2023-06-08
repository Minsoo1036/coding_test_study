## 백준 온라인 저지 시뮬레이션 문제 14503번 - 로봇 청소기

N, M = map(int,input().split())

r, c, d = map(int,input().split())

room = []
for i in range(N):
  room.append(list(map(int,input().split())))

mark_map = []
for i in range(N):
  mark_map.append([0]*M)

direction_li = [0,1,2,3] #북, 동, 남, 서 순
dx = [0,1,0,-1]
dy = [-1,0,1,0]

pos_x = c
pos_y = r
mark_map[pos_y][pos_x] = 1
tol = 0
count = 1
d = (d-1) % 4

while room[pos_y][pos_x] != 1 :
  if room[pos_y + dy[d]][pos_x+dx[d]] == 0 :
    if mark_map[pos_y + dy[d]][pos_x+dx[d]] == 0:
      pos_x += dx[d]
      pos_y += dy[d]
      mark_map[pos_y][pos_x] = 1
      tol = 0
      count += 1
      d = (d-1) % 4
      tol += 1
    else:
      if tol == 4 :
        pos_x -= dx[d]
        pos_y -= dy[d]
        tol = 0
        d = (d-1) % 4
        tol += 1
        #count += 1
      else:
        d = (d - 1) % 4
        tol += 1

  else:
    if tol == 4:
      pos_x -= dx[d]
      pos_y -= dy[d]
      tol = 0
      d = (d-1) % 4
      tol += 1
      #count += 1
    else:
      d = (d-1) % 4
      tol += 1
    
print(count)
