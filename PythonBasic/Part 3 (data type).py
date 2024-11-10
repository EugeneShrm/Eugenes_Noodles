# Numeric data types: int, float, and complex
num1 = 6
print(num1, 'is of type', type(num1))
num2 = 3.0
print(num2, 'is of type', type(num2))
num3 = 2 + 4j
print(num3, 'is of type', type(num3))

# A list is an ordered sequence of elements of the same or different types, separated by commas and enclosed in square brackets [ ]
languages = ["Docker", "Java", "Python"]
# Accessing the element with index 0
print(languages[0])  # will print Docker
# Accessing the element with index 2
print(languages[2])  # will print Python

# A tuple is similar to a list. The only difference is that tuples are immutable. Created tuples cannot be changed.
# Create a tuple
product = ('Sony', 'PlayStation', 599.99)
# Accessing the element with index 0
print(product[0])  # will print Sony
# Accessing the element with index 1
print(product[1])  # will print PlayStation

# str in Python
name = 'Python fffffffff'
print(name)  
message = 'Python for beginners'
print(message, name)

# Set - A set is an unordered collection of unique elements. The collection contains values separated by commas inside curly braces { }
# Create a set student_id
student_id = {112, 114, 116, 118, 115}
# Output the elements of the set student_id
print(student_id)
# Output the data type of the set student_id
print(type(student_id))

# dict - A dictionary is an ordered set of elements. It stores elements in key-value pairs. Keys are unique identifiers associated with values.
# Create a dictionary capital_city
capital_city = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
print(capital_city)

# Create a dictionary capital_city. Keys are used to access values. The opposite does not work.
capital_city = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Japan': 'Tokyo'} 
print(capital_city['Ukraine'])  # will print Kyiv
