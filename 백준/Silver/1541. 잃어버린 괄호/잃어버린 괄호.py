a = input().split('-')
if len(a) == 1:
  b = a[0].split('+')
  total = 0
  for i in b:
    total += int(i)
  print(total)
elif len(a) >= 2:
  for aa in range(len(a)):
    total = 0
    b = a[aa].split('+')
    for i in b:
      total += int(i)
    a[aa] = total
  all_total = int(a[0])
  for num in a[1:]:
    all_total -= int(num)
  print(all_total)