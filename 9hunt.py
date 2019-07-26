u=int(input(""))
u1=list(map(int,input().split()))
o=len(u1)
large=max(u1)
y,z=0,0
for i in range(0,o-1):
 for j in range(i+1,o):
  if abs(u1[i]+u1[j])< large:
   y,z=u1[i],u1[j]
   large=abs(y+z)
print(y, z)
