#백준 구현 문제 - 10871번, X보다 작은 수

N, X = map(int,input().split())

numbers = list(map(int,input().split()))

for k in numbers:
  if k < X :
    print(k, end=' ')

#시간복잡도 : O(N)
  