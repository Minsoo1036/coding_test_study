# Greedy - 백준 2839번 (설탕배달)
## 문제풀이 아이디어 : 5가 최대한 채워지고 나머지를 3이 채워야 가장 적은 수로 채워질 것이다. 따라서 5를 최대한으로 채워넣고 만약 나누어 떨어지지 않는다면 5를 하나씩 빼면서 그 나머지를 3으로 나누어 떨어지면 차선책으로 그 자리를 3으로 메꾼다. 5를 다 뺐는데도 3으로도 다 채워지지 않는다면 -1을 도출한다.

## 시간 복잡도 : 최선의 경우: O(1), 최악의 경우 : O(N/5)

N = int(input())

if N >= 5 :
  if N % 5 == 0 :
    answer = int(N/5)
  elif N % 5 == 3 :
    answer = int(N/5) + 1
  else:
    spare = int(N % 5)
    for i in range(1,int(N/5)+1,1):
      spare = spare + 5 
      if spare % 3 == 0 :
        answer = int(spare / 3) + int(N/5) - i 
        break
      if i == int(N/5):
        answer = -1
else:
  if N == 3 :
    answer = 1
  else:
    answer = -1
  
    
print(answer)