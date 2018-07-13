a=int(input())
l=[1]
b=0
c=1
for i in range(0,a-1):
  x=b+c
  l.append(x)
  b=l[i]
  c=l[i+1]
print(l)  
