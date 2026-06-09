val =  input()
map = {'A':'T','T':'A','C':'G','G':'C'}

lst =[]

for i in val:
  lst.append(map[i])
rev = lst[::-1]
print("".join(rev))
