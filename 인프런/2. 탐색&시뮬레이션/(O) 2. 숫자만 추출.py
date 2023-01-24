import sys

input=sys.stdin.readline

N=input().strip()

num=0
for i in N:
  if 48<=ord(i)<=57: # i.isdecimal(), i.isdigit()
    num=num*10+int(i)

cnt=0
for i in range(1,num+1):
  if num%i==0:
    cnt+=1

print(num)
print(cnt)
  