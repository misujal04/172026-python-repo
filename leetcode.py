
num=input (str("enter"))
new=len(num)
print(num[0],end="")
for i in range(1,new):
    if i%2==0:
        print(num[i],end="")
    else:
        print(num[i].swapcase(),end="")