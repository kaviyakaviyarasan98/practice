num=int(input())
s=""
n=num
while n!=0:
    rem=n%10
    n=n/10
    s=s+str(rem)
num=str(num)
if s==num:
    print("palindrome")
else:
    print("not a palindrome")
