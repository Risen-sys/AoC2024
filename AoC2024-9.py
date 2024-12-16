"""
F,S,p=[],[],0
for i, c in enumerate(open(r'C:\\Users\\MatthewSilbernagel\\Desktop\\input.txt').read().strip()):
    [F,S][i%2] += [[*range(p,p:=p+int(c))]]
S = sum(S,[])
for f in reversed(F):
    for x in reversed(range(len(f))):
        if len(S) and f[x] > S[0]:
            f[x] = S[0]
            S = S[1:]
print(sum((i*j) for i,f in enumerate(F) for j in f))
"""



F,S,p=[],[],0
for i, c in enumerate(open(r'C:\\Users\\MatthewSilbernagel\\Desktop\\input.txt').read().strip()):
    [F,S][i%2] += [[*range(p,p:=p+int(c))]]
for y in reversed(range(len(F))):
    for x in range(len(S)):
        if len(S[x]) >= len(F[y]) and F[y][0] > S[x][0]:
            F[y] = S[x][:len(F[y])]
            S[x] = S[x][len(F[y]):]
print(sum((i*j) for i,f in enumerate(F) for j in f))