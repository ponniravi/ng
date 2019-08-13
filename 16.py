m=int(input())
t=list(map(int,input().split()))
s=[]
for i in t:
    if t.count(i)>1:
        s.append(i)
if s==[]:
    print("unique")
else:
    print(s[0])
