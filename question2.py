# Question 2: Comparison and Logical Operators

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

# TODO: Create a condition that checks if a is greater than b
if a > b :
  print("a is greater than b")
else :
  print("b is greater than a")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 == 0:
  print("b is even")
else :
  print("b is odd")

# TODO: Create a condition that checks if c is less than or equal to a
if c <= a :
  print("c is less than or equal to a")
else :
  print("c is greater than a")

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a > b) or (b % 2 == 0) and (c <= a)

# TODO: Print the value of 'final_condition'
print(final_condition) 