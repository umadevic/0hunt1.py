u=input().split()
A=input().split()
B=input().split()
A.sort()
B.sort()
p=0
for i in B:
    if i in A:
        p=p+1
if p==len(B):
    print('Yes')
else:
    print('No')
