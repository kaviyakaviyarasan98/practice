num=raw_input()
n=len(num)
num=int(num)
num1=num
a=0
while num1!=0:
    rem=num1%10
    num1=num1/10
    b=rem**n
    a=b+a
if a==num:
    print("armstrong number")
else:
    print("not a armstrong number")
