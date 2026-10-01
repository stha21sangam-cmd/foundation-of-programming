# for single line comment shit + control
""" 
for multiple line alt+shit+a python is dynamically type so no declare
 """
name = input("enter your name")
age = int(input("enter your age"))
location = input("enter your location")
print('my name is '+name+'age is '+str(age)+" location is"+location)
#fstring
print(f'my name is {name} age is {age} and my location is {location}')
#format old version
print('my name is %s age is %d and location is %s'%(name,age,location))
#format new version
print("my name is {}age is {} and location is {}".format(name,age,location))

print(type(location))

num1 = input("enter the num1:")
num2 = input("enter the num2:")
sum1 = num1 + num2
print("the sum is"+sum1+"and the type is"+type(sum1))


num3 = input("enter the num1:")
num4 = input("enter the num2:")
sum2 = num1 + num2
print("the sum is "+ sum2 +"and the type is "+type(sum1))