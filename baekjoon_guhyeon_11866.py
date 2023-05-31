# 백준 11866번 문제 - 요세푸스 문제 0

N, K = map(int,input().split())

num_array = [i for i in range(1,N+1,1)]
del_idx = 0

mark_li = []
while len(num_array) > 0 :
  del_idx = (del_idx + (K-1)) % len(num_array)
  mark_li.append(str(num_array[del_idx]))
  del num_array[del_idx]


print("<"+", ".join(mark_li)+">")

#시간 복잡도 O(N)
  
  