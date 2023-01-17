m,n,a=map(int,input().split())
if m%a==0:
    value1=m//a
else:
    value1=m//a + 1
if n%a==0:
    value2=n//a
else:
    value2=n//a +1
print(value1*value2)
