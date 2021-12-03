#Program to input a three subjects marks of student out of 100 and calculating average and percentge of that marks.
print('Enter the three subjects marks out of 100')
m1=float(input('Enter the first subject marks: '))
m2=float(input('Enter the second subject marks: '))
m3=float(input('Enter the third subject marks: '))
sum=m1+m2+m3
avg=sum/3
per=(sum/300)*100
print('Average marks obtained: ',avg)
print('Percentage obtained: ',per)