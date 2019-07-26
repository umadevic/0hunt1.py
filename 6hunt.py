t1=int(input())
x=list(map(int,input().split()))
x.sort()
s=[]
for i in range(len(x)-1):
    if l[i]==l[i+1]:
        s.append(x[i])

if r:
    for j in set(s):
        print(j,end=" ")
        break
else:
    print("unique")
© 2019 Git
