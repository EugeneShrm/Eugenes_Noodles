# function Map
# when we don't want to use cykle and we need to do the same action for each item
def add_greeting(name):
    return 'Hello, ' + name

name = ['John', 'Eugene', 'Anna']

nameGreeting = map(add_greeting, name)

print(name)
print(list(nameGreeting))
print()
# lambda instead of funct

names = ['John', 'Eugene', 'Anna']

nameGreeting = map(lambda name: 'Hello, ' + name, names)

print(list(nameGreeting))

# functin flter
names = ['John', 'Eugene', 'Anna', 'Olha']
def check_name(name):
    if 'o' in name:
        return False
    elif 'O' in name:
        return False
    return True
filtered_names = list(filter(check_name, names))
print(filtered_names)

# function Zip
# we have a 2 lists: names and data birth and we need to match it togather

names = ['John', 'Eugene', 'Anna']
years = [1990, 1992, 1995]

nameYears=list(zip(names, years))

print(nameYears)
print(nameYears[1])
print()

