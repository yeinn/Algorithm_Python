import sys
#sys.stdin=open("input.txt","rt")

s= input('')
num=0
cnt=0

for i in s:
    if i.isdigit()==True:
        num=num*10+int(i)

for i in range(1,num+1):
    if num%i==0:
        cnt+=1

print(num)
print(cnt)

