u=list(map(str,input().split()))
o=[]
for i in u:
	p=i[::-1]
	o.append(p)
for j in o:
	print(j,end=" ")
