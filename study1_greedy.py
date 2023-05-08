# 1이 될때 까지 (나동빈, 코딩테스트)

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
print(n, m, k )
data.sort()
print(data[-1])

first = int(m/k) * k
second = m%k
print("first",first)
print("second",second)

print(data[-1] * first + data[-2] * second)

#print(data[-1]*(k-1))
