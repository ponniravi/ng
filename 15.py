z=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
u=[]
for i in range(z):
    u.append(l[i]+m[i])
print(*u)   
