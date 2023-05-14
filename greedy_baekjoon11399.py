## 그리디문제 - 백준 11399번 (ATM)
 
N = int(input())
P = list(map(int,input().split()))
P.sort(reverse=True)
#print(P)

answer = 0 
for i in range(1,N+1,1):
  #print(P[i-1] * i)
  answer += P[i-1] * i

print(answer)

# 시간복잡도 : O(Nlog(N)+N)  

"""
N=int(input())
P=list(map(int, input().split()))

P.sort() #O(NlogN)

totalSec=0
for i in range(N): 
  totalSec+=sum(P[:i+1]) 
  
print(totalSec)

# 시간 복잡도 : O(Nlon(N)+N^2)
"""