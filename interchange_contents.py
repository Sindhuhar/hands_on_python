#python program to swap two numbers using temporary variable
x=input('Enter value of x: ')
y=input('Enter value of y: ')
temp=x
x=y
y=temp
print('The value of x after swapping: ',x)
print('The value of y after swapping: ',y)

#Without using temporary variable
x=input('\nEnter value of x: ')
y=input('Enter value of y: ')
x,y=y,x
print('The value of x after swapping: ',x)
print('The value of y after swapping: ',y)
