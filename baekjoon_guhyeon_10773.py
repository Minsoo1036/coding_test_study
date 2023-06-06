#백준 구현 문제(10773) - 제로

K = int(input())

num_li = []
for i in range(K):
  add_num = int(input())
  if add_num == 0:
    num_li.pop(-1) #가장 최근에 들어간거 out
  else:
    num_li.append(add_num)

answer = sum(num_li)
print(answer)

# 시간복잡도 : O(K)
