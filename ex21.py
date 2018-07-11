def kavi(a,b,c):
  sum=0
  i=0
  while(i<a):
    sum=sum+b
    b=b+c
    i=i+1
  return sum
a=int(input(""))
b=int(input(""))
c=int(input(""))
print(kavi(a,b,c))
