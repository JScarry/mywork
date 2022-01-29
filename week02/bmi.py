#Body mass index calculator
#Author Jarlath Scarry

name = input ('Enter your name:')
print ('Hello {}\n Please answer the following questions and we\
    \n will calculate your Body Mass Index (BMI)\n'.format(name))

age = input ('What is your age?:')
weight = float(input ('What is your weight(KG)?:'))
height = float(input ('What is your height(CM)?:'))

print ('Your age is {} , weight {}KG and height is {}CM.\n'.format(age, weight, height))

#ans = input ('Are these details correct? y/n\n')
#print (ans)

bmi = weight / (height/100)**2

print ('{} your BMI is {:.2f}' .format(name,bmi))






