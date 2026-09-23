
sum=0

while(num!=0):
    rem=num%10
    num=num//10
    sum=sum*10+rem
    count=count+1
print(sum)
