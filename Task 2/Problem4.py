
def pos(p,g):
  p = []
  k =  len(p)
  for i in range(len(g)-k+1):
    if g[i:i+k] == p:
      p.append(i)
  return p
