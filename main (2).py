#나동빈 코딩테스트, 왕실의 나이트 (구현 문제)
pos = input()
start_row = int(pos[1])
start_col = pos[0]

idx = 1
for k in ["a","b","c","d","e","f","g","h"]:
  if k == start_col:
    start_col = idx
  idx += 1

dcol = [-2,-2,2,2,-1,1,-1,1]
drow = [1,-1,1,-1,2,2,-2,-2]

count = 0
for k in range(8):
  if start_col + dcol[k] < 1 or start_col + dcol[k] > 8  :
    continue
  if start_row + drow[k] < 1 or start_row + drow[k] > 8  :
    continue
  count+=1

print(count)

#시간 복잡도 : O(1)