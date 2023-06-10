#백준 시뮬레이션 문제 3190번 - 뱀

N = int(input())
K = int(input())

apple_map = []
for k in range(N): #사과의 위치를 기록.
  apple_map.append([0] * N)

body_map = []
for k in range(N): #자기 몸의 위치를 기록.
  body_map.append([0] * N)

for k in range(K):
  y, x = map(int,input().split()) #행,열을 순서대로 받음.
  apple_map[y-1][x-1] = 1

#print(apple_map)

L = int(input())
schedule_li = []

for k in range(L):
  t, d = input().split()
  schedule_li.append((int(t),d))

#print(schedule_li[0][0])

direction_li = [0,1,2,3] #북, 서, 남, 동 순
dx = [0,-1,0,1]
dy = [-1,0,1,0]
d = 3 #동쪽방향으로 시작.
t = 0
pos_x = 1
pos_y = 1
record_li = [] #몸의 순서를 기록.
record_li.append((pos_x,pos_y))
body_map[pos_y-1][pos_x-1] = 1

while True:
  ## print("direction" , d)
  if pos_x + dx[d] < 1 or pos_x + dx[d] > N :
    t+=1
    break
  if pos_y + dy[d] < 1 or pos_y + dy[d] > N : 
    t+=1
    break
  if body_map[pos_y +dy[d] -1][pos_x + dx[d] -1] == 1:
    t+=1
    break
  pos_x += dx[d]
  pos_y += dy[d]
  ## print(pos_x,pos_y)

  body_map[pos_y-1][pos_x-1] = 1 #옮긴다음에 머리 표시
  record_li.append((pos_x,pos_y))
  ## print(record_li)
  
  if apple_map[pos_y-1][pos_x-1] == 1:
    apple_map[pos_y-1][pos_x-1] = 0
  else:
    tail_x, tail_y = record_li.pop(0)
    body_map[tail_y-1][tail_x-1] = 0
    
    

  #if body_map[pos_y-1][pos_x-1] == 2:
  #  t+=1
  #  break
    
  t+=1

  if len(schedule_li) == 0:
    continue
  
  if t == schedule_li[0][0]: #끝나기 직전에 방향 물어봄
    ## print("yes")
    if schedule_li[0][1] == "L":
      d = (d+1) % 4
    else:
      d = (d-1) % 4
    schedule_li.pop(0)
      #print(d)
  #print(pos_x,pos_y)
  
    

print(t)
  
  
  
