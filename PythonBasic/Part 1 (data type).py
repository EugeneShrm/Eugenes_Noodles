a = 1
b = 2.5
c = "I will create the best AI ever"

# You can also write variables in one line
a, b, c = 1, 2.5, 'I will create the best AI ever'

print(a, ',', b, ',', c, '!')
print(a, b, c, sep=',', end='!')

# To find out the data type, you need to add type
print(type(a))
print(type(b))
print(type(c))

# List - [] is an ordered sequence of elements of the same or different types, separated by commas and enclosed in square brackets [
varList = [1, 2, 3, 4]
varList[2] = 100000

# Indexing in Python starts from 0
print(varList[0])

# Slicing
print(varList[0:2])

# From the second element
print(varList[2:])

# Tuple = similar to a list. The only difference is that the data in a tuple is immutable.
varTuple = (1, 1, 2, 3, 5, 8, 13)
# e.g., assigning a value is not possible - varTuple[2] = 100000

# str in Python
name = 'Python'
print(name)

# Set - { } - a collection of unordered elements
# Create a set student_id
student_id = {112, 114, 116, 228, 115}
# Output the elements of the set student_id
print(student_id)
# but print(student_id[0]) will not work, sets are just for adding data

# dict - A dictionary is an ordered set of elements. It stores elements in key-value pairs. Keys are unique identifiers associated with values.
# Create a dictionary capital_city
capital_city = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
print(capital_city)

# INFORMATION FROM THE INTERNET ABOUT DATA TYPES
# Numeric data types: int, float, and complex
num1 = 6
print(num1, 'is of type', type(num1))
num2 = 3.0
print(num2, 'is of type', type(num2))
num3 = 2 + 4j
print(num3, 'is of type', type(num3))

# List - is an ordered sequence of elements of the same or different types, separated by commas and enclosed in square brackets [ ]
languages = ["Docker", "Java", "Python"]
# Access the element with index 0
print(languages[0])  # will print Docker
# Access the element with index 2
print(languages[2])  # will print Python

# Tuple - similar to a list. The only difference is that tuples are immutable. Created tuples cannot be changed.
# Create a tuple
product = ('Sony', 'PlayStation', 599.99)
# Access the element with index 0
print(product[0])  # will print Sony
# Access the element with index 1
print(product[1])  # will print PlayStation

# str in Python
name = 'Python'
print(name)
message = 'Python for beginners'
print(message)

# Set - A set is an unordered collection of unique elements. The collection contains values separated by commas inside curly braces { }
# Create a set student_id
student_id = {112, 114, 116, 118, 115}
# Output the elements of the set student_id
print(student_id)
# Output the data type of the set student_id
print(type(student_id))

# dict - A dictionary is an ordered set of elements. It stores elements in key-value pairs. Keys are unique identifiers associated with values.
# Create a dictionary capital_city. Keys are used to access values. The opposite does not work.
capital_city = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
print(capital_city['Ukraine'])  # will print Kyiv
print(capital_city['Spain'])
