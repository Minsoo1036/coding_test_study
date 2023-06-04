#백준 시뮬레이션 문제 - 1966번 프린터 큐

n_test = int(input())

count_li = []
for k in range(n_test):
  N, M = map(int,input().split())
  import_li = list(map(int,input().split()))
  record_li = [i for i in range(N)]

  count = 0
  while len(import_li) != 0:
    if len(import_li) == 1:
      out = import_li.pop(0)
      record_out = record_li.pop(0)
      count+=1
      if record_out == M :
        break
        
    if import_li[0] < max(import_li[1:]):
      out = import_li.pop(0)
      import_li.append(out)
      record_out = record_li.pop(0)
      record_li.append(record_out)
      
    else:
      out = import_li.pop(0)
      record_out = record_li.pop(0)
      count+=1
      if record_out == M :
        break
  count_li.append(count)

for i in range(n_test):
  print(count_li[i])