#백준 그리디 문제 - 잃어버린 괄호 (1541번)

d = input()
#print(d.split("-"))
e = d.split("-")
#print(e[0].split("+"))
#print(e[1].split("+"))

count = 0
answer = 0
for k in e :
  split_k = k.split("+")
  sum_k = 0
  for j in split_k :
    sum_k += int(j)
  count += 1
  if count == 1 : #첫번째 식
    answer = sum_k
  else:
    answer -= sum_k

#print(int('00009'))
print(answer)

