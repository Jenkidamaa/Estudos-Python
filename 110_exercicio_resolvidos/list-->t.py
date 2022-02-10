def exercicios075():
  l = []
  a = 0
  a9 =0
  a2 =0
  p = 0
  for i in range(4):
    a = int(input())
    l.append(a)
  t = tuple(l)
  for i in t:
    if i>9:
      a9 += 1
    
    if i%2 == 0:
      a2 = 0
  print(t)
  print(t.count(9) , t.index(3))
exercicios075()
