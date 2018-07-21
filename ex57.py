def countx(l,c):
  count=0
  for i in l:
    if(i==c):
      count=count+1
  return count
a=int(input())
c=int(input())
l=[]
for i in range(0,a):
  b=int(input())
  l.append(b)
print(countx(l,c))
