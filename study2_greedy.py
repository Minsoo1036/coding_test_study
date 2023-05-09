### 숫자 카드 게임
n, m = map(int,input().split())

row_li = []
for k in range(n):
  temp_li = list(map(int,input().split()))
  temp_li.sort()
  row_li.append(min(temp_li))
  #print(min(temp_li))
answer = max(row_li)
print(answer)

# 시간 복잡도 : O(N*(M+1))