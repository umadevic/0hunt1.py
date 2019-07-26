t1=int(input())
l=list(map(int,input().split()))
l.sort()
s=[]
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        s.append(l[i])

if s:
    for j in set(s):
        print(j,end=" ")
        break
else:
    print("unique")
