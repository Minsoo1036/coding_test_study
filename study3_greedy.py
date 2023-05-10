# 1이 될때까지

n, k = map(int, input().split())

count = 0
while n !=1 :
  if n % k == 0 :
    n = n / k
  else:
    n = n - 1
  count += 1

print(count)

# 최악의 경우 : O(N)
# 최선의 경우 : O(log_{K}^{N})
  