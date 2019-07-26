r=int(input())
q=list(map(int,input().split()))
k=[]
for i in range(0,len(q)):
    if q[i]%2==0 and i%2==1:
        k.append(q[i])
    elif q[i]%2==1 and i%2==0:
        k.append(q[i])
print(*k,sep=' ')
