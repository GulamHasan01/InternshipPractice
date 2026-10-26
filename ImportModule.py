
#import helper as hp
from helper import addition as add, subtraction as sub, multiplication as mul
print("Enter operands")
a=float(input())
b = float(input())
print("enter operator: +,/,*,-")
c=input()
ans=0
if c=="+":
    ans=add(a,b)
elif c=="-":
    ans=sub(a,b)
elif c=="*":
    ans=mul(a,b)
print(ans)