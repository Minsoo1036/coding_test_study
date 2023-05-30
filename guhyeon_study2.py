#나동빈 구현 문제 - 게임 개발

N, M = map(int, input().split()) #세로, 가로

A, B, d = map(int,input().split())

game = []
for k in range(N):
  game.append(list(map(int,input().split())))

game_mark = []
game_mark.append((B+1,A+1))      


direction_li = [0,1,2,3] #북,동,남,서 순
dx = [0,1,0,-1]
dy = [-1,0,1,0]

direction = d
x = B+1
y = A+1
tol = 0 #방향 바꾸는 한계

print(game_mark)
print(game)


while game[y-1][x-1] == 0 :
  
  if game[y + dy[d] - 1][x + dx[d] - 1] == 0: #육지였을때
    if (x+dx[d],y+dy[d]) not in game_mark: 
      y = y + dy[d]
      x = x + dx[d]
      print(x,y)
      tol = 0
      game_mark.append((x,y))
      #print(game_mark)
      #print(x,y)
    else:
      if tol == 4:
        y = y - dy[d]
        x = x - dx[d]
        print(x,y)
        tol = 0
      else:
        d = direction_li[(d-1)%4]
        tol += 1
        print(x,y)
  else: #바다였을때
    if tol == 4:
      y = y - dy[d]
      x = x - dx[d]
      print(x,y)
      tol = 0
    else:
      d = direction_li[(d-1)%4]
      #print(d)
      tol += 1
      print(x,y)

answer = len(game_mark)
print(answer)
 