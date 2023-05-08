# 1이 될때 까지 (나동빈, 코딩테스트)

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
print(n, m, k )
data.sort() #sorting the list
print(data[-1])

num_blocks = m // (k+1)
spare = m % (k+1)

answer = (data[-1] * k + data[-2]) * num_blocks + data[-1] * spare

print(answer)
