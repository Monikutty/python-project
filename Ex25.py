a=int(input())
l=[]
for i in range(0,a):
  b=int(input())
  l.append(b)
  l.sort()
if(a%2==0):
  x=(l[a//2]+l[a//2-1])/2
else:
  x=l[(a-1)//2]
print(x)
