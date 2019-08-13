p,k=map(str,input().split())
k=int(k)
a=[]
for i in range(len(p)):
    if len(p[i:i+k])==k:
        a.append(p[i:i+k])
print(*a)
#i
