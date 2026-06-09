def pos(p,g):
  res = []
  k =  len(p)
  for i in range(len(g)-k+1):
    if g[i:i+k] == p:
      res.append(i)
  return res
p = input()
g = input ()
r = pos(p,g)
print(*r)
