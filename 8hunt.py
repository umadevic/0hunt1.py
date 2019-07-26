m1=int(input())
m2=list(map(int,input().split()))
for i in range(0,m1-2):
 for j in range(i+1,m1-1):
  for k in range(j+1,m1):
   if(m2[i]+m2[j]==m2[k]):
    print(m2[i], m2[j], m2[k])
