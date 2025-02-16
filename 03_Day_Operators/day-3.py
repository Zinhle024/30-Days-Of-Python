# Arithmetic Operations in Python
# Integers

#Q1
age = 1
#Q2
my_height = 158.0
#Q3
complex_num = 10j

#Area of triangle Q4
height = input("What is the height of a triangle? ")
base = input("What is the base of a triangle? ")
area = 0.5 * int(base) * int(height)

print(f"The area of the triangle is {area}")

#Perimeter of a triangle Q5

side_a = input("How long is side a ?")
side_b = input("How long is side b ?")
side_c = input("How long is side c ?")
perimeter = int(side_a) + int(side_b) + int(side_c)

print(f"The triangles perimeter is {perimeter}")


#Rectangle area,periemter Q6

rect_length = input("What is length of the rectangle? ")
rect_width = input("What is width of the rectangle? ")
rect_area = int(rect_length) * int(rect_width)
rect_perimeter = (int(rect_length) + int(rect_width)) * 2

print(f"The area of the rectangle is:{rect_area}")
print(f"The perimeter of the rectangle is:{rect_perimeter}")

#CIRCLE Q7

radius = input("What is the radius of the circle? ")
pi = 3.14
circle_area = int(radius)*int(radius)*pi
circle_circumference = 2 * pi * int(radius)

print(f"The area of the circle is: {circle_area}")
print(f"The circumference of the circle is: {circle_circumference}")

#Slope  Q8
equation = "y = 2x - 2".replace(" ", "")
slope = int(equation[2])
y = (int(equation[2]) * 0 ) - int(equation[5])
x = int(equation[2]) / int(equation[5])
y_int = (0,int(y))
x_int = (int(x),0)

print(f"The slope is: {slope}\n The y-intercept is : {y_int}\n The x-intercept is: {x_int}")

#Slope Q9 (m = y2-y1/x2-x1) points: (2, 2) (6,10)

point1 = (2, 2)
point2 = (6,10)

slope2 = int((point2[1] - point1[1]) / (point2[0] - point1[0]))
y_2 = point1[1] - slope2 * point1[0]
x_2 = point2[0] - slope2 * point2[1]
y_intercept = (0,int(y_2))
x_intercept = (int(x_2),0)
print(f"The second slope is: {slope2}\n The y-int: {y_intercept}\n The x-int: {x_intercept}")

#Q10
print(f"Slopes are equal{slope == slope2}")

#Q11
x = -3
y = (x ** 2) + (6 * x) + 9
print(f"The value of y is: {y}\n")
print(f"The value of x that will give zero as an answer is: {x}\n")

#Q12
if len("python") == len("dragon"):
    print(not not True)

#Q13
print("on" in "python" and "on" in "dragon")

#Q14
print("jargon" in "I hope this course is not full of jargon")

#Q15
if "on" in "python" and "on" in "dragon":
    print(not True)

#16
print(float(len("python")))
print(str(len("python")))
    
#Q17
i = 2
if i % 2 == 0:
    print("EVEN")

#Q18
print(7//3 == int(2.7))

#Q19
print(type("10") == type(10))

#Q20
print(int(9.8) == 10)

#Q21
hours = input("How many hours have you worked this week? ")
rate = input("What is your hourly rate? ")
weekly_earning = int(hours) * int(rate)

print(f"Your weekly earning is: {weekly_earning}")

#Q22
years = input("How many years have you lived? ")

seconds = int(years) * 31536000
if seconds > 3153600000:
    print("YOU ARE TOO OLD")

print(f"You have live for {seconds} seconds")





















print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False