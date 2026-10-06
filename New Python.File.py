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


num1 = input("enter the num1:")
num2 = input("enter the num2:")
sum1 = num1 + num2
print("the sum is"+ sum1 +"and the type is" + str(type(sum1)))


num3 = input("enter the num1:")
num4 = input("enter the num2:")
sum2 = num3 + num4
print("the sum is " + sum2 +"and the type is " + str(type(sum2)))

print(ord('a'))
print(ord('🎲'))


print(chr(67))
print('apple'<'Apple') #because of ascil value of a is greater than A

print('Hello my name is prajwol and I believe in the quote\"hello this is my life\"')

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================

a = 10
b = 3

print("Addition:", a + b)        # +  → 10 + 3 = 13
print("Subtraction:", a - b)     # -  → 10 - 3 = 7
print("Multiplication:", a * b)  # *  → 10 × 3 = 30
print("Division:", a / b)        # /  → 10 ÷ 3 = 3.333...
print("Floor Division:", a // b) # // → removes decimal → 3
print("Modulus:", a % b)         # %  → remainder → 1
print("Power:", a ** b)          # ** → 10³ = 1000


# ==========================================
# 2. COMPARISON OPERATORS
# ==========================================

print(a == b)   # == → equal to?        False
print(a != b)   # != → not equal?       True
print(a > b)    # >  → greater than?    True
print(a < b)    # <  → less than?       False
print(a >= b)   # >= → greater/equal?   True
print(a <= b)   # <= → less/equal?      False


# ==========================================
# 3. ASSIGNMENT OPERATORS
# ==========================================

x = 10          # =  → put 10 into x

x += 5          # += → x = x + 5
print(x)        # 15

x -= 3          # -= → x = x - 3
print(x)        # 12

x *= 2          # *= → x = x * 2
print(x)        # 24

x /= 4          # /= → x = x / 4
print(x)        # 6.0


# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================

age = 20
has_id = True

print(age > 18 and has_id)
# and → BOTH conditions must be True
# True and True → True

print(age > 18 or has_id)
# or → AT LEAST ONE condition must be True
# True or True → True

print(not has_id)
# not → reverses True/False
# not True → False


# ==========================================
# 5. BITWISE OPERATORS
# ==========================================

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(a & b)   # &  → AND → 0001 → 1
print(a | b)   # |  → OR  → 0111 → 7
print(a ^ b)   # ^  → XOR → 0110 → 6
print(~a)      # ~  → NOT → -6

print(a << 1)  # << → shift bits left  → 1010 → 10
print(a >> 1)  # >> → shift bits right → 0010 → 2


a = [2,3,4]
b = [2,3,4]
c=a
print(a is b)
print (a is c)
print(a==b)
print (a==c)
print(id(a))
print(id(b))
print(id(c))


#assignment operator
print(5==6)