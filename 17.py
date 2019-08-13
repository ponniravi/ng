t=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(t):
    if m[0]==l[i]:
        print(i)
