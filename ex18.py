num=int(input(""))
a=int(input(""))
b=int(input(""))
for num in range(a,b+1):
  x=len(str(num))
  sum=0
  temp=num
  while(temp>1):
    digit=temp%10
    sum+=digit**x
    temp=temp/10
if(num==sum):
  print(num)
