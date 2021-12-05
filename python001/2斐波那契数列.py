#递归法
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(1,21):
    print(fib(i),end=" ")

#for循环
def fib(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
    return a
for i in range(20):
    print(fib(i),end=" ")
input()
