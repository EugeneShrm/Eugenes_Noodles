def print_greeting():
    """
    Print 'Hello' text
    :return: None
    """
    print("Hello") # function body
print_greeting() # Call the function
help(print_greeting) # function documentation / doc str


def print_greeting():
    """
    Print 'Hello' text
    """
    print('Hello')  # function body

print_greeting() # Call the function

# Display the function's documentation (docstring)
# help(print_greeting)

def greeting_withName(name = "Name"):
    """
    :param name
    :returt: None
    """
    print('Hello ' + name + '!')

# help(greeting_withName)
greeting_withName("Eugene")
greeting_withName("Anna")
greeting_withName()

def sum_of_2numbers (a = 1, b=2):
    '''
    :param a: the first addednt
    :param b: the second addednt
    :return: sum of a and b
    '''
    return (a+b)

x = sum_of_2numbers(2, 3)
print(x)
# help(sum_of_2numbers)

def hello_in_text (text = 'Hello'):
    if "Hello" in text:
        return True
    elif "hello" in text:
        return True  
    else:
        return False 
print(hello_in_text("say hello everybody"))

# shorter variant
def hello_in_text2 (text = 'Hello'):
    return "Hello" in text.capitalize()
print(hello_in_text2("hello there"))

def string_in_text (string, text):
    return string in text
print(string_in_text("app", "is the apple"))

def gender_greeting (name, gender):
    if gender == "male":
        print("Hello " + name + " you are great man")
        return gender
    elif gender == "female":
        print("Hello " + name + " you are so betaful")
        return gender
    else:
        print("Hello " + name + " you are LGBT")
        return gender

value1 = gender_greeting("Eugene", "male")
value2 = gender_greeting("Anna", "female")
value3 = gender_greeting("Tokyo", "dog no boy no girl")

