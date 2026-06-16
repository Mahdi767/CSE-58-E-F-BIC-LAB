
x =  input()
y = input()

d = int(input())


def hm_d(s1,s2):
    mis_cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mis_cnt+=1
    return mis_cnt

def pattern_match(p,t,d):
    pos = []
    k =  len(p)
    
    for i in range(len(t)-k+1):
        win = t[i:i+k]
        
        if hm_d(p,win) <=d:
            pos.append(i)
    return pos

res = pattern_match(x,y,d)
print(*res)
