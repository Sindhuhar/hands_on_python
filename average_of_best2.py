#Write a python program to find the best of two test average marks out of three tests marks accepted from the user.
m1=int(input('Enter the test 1 marks: '))
m2=int(input('Enter the test 2 marks: '))
m3=int(input('Enter the test 3 marks: '))
minimum=min(m1,m2,m3)
sumofbest2=m1+m2+m3-minimum
avgofbest2=sumofbest2/2
print('Average of best two= ',avgofbest2)
