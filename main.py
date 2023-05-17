## 백준 그리디 문제 -1931번 회의실 배정
N = int(input())

sc_dict = dict()
for k in range(N):
  a, b = map(int, input().split())
  if a in list(sc_dict):
    if sc_dict[a] > b:
      sc_dict[a] = b
  else:
    sc_dict[a] = b

inv_sc_dict = {v: k for k, v in sc_dict.items()} #딕셔너리 서칭타임이 오래걸리는듯
end_li = sorted(list(inv_sc_dict))

count = 0
for k in end_li:  #제일 빨리 끝나는 애들부터
  if count == 0:  #첫번째 방문자
    start = inv_sc_dict[k]
    end = k
    count += 1
    print(start,end)
  else:
    if inv_sc_dict[k] >= end:
      start = inv_sc_dict[k]
      end = k
      count += 1
      print(start,end)

print(count)

#시간 복잡도 : O(NlogN + 3*N)
