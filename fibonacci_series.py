#Program to get the Fibonacci series between 0 to n.
x,y=0,1
n=int(input('Enter the number: '))
while y<n:
    print(y)
    x,y=y,x+y