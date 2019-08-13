t,k=map(int,input().split())
c=0
if k>t:
    print(0)
else:
    while t>0:
        t=t-k
        c=c+1
    if t==0:
        print(c)
 #i
