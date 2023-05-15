## 백준 그리디 문제 - 11047번 동전 O

N, K = map(int, input().split())

value_li = []
for i in range(N):
  value_li.append(int(input()))

value_li.sort(reverse=True)

#print(value_li)

count = 0 
for i in value_li:
  if K == 0 :
    break
  if int(K/i) >= 1 :
    count += int(K/i)
    K = K % i

print(count)

#시간 복잡도 : O(Nlog(N) + N)