a=int(input())
temp=0
while(a>1):
  b=a%10
  temp=temp+b
  a=a/10
c=int(temp)
print(c)
