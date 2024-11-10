#functions
#1
def sayBuy(name: str):
    print("Buy," + name)
sayBuy("Bob")

print()

#2
def sayNum(num: float):
    print("Hello, " + str(num)) # not right - print("Hello, " + num)
sayNum(10.111111)
print()

#3
def sayHello(fName: str, sName: str,) -> str:
    return "Hello, "+fName+ " "+sName
message = sayHello("Joe", "Black") # message = sayHello(fName = "Joe", sName = "Black")
print(message)

print()

#4
def sayHello2(*names) -> str: #dovilna kilkist parametriv
    print(names[1])
    
sayHello2("Joe", "Black")
print()

#5
def sayHello2(**names) -> str: #dictionary
    #print(names)
    return "Hello, " +names["fName"]+ " " + names["sName"]
    
message=sayHello2(fName = "Joel", sName = "Last")
print(message)

#6
def sayHello3(**names) -> str:  # Dictionary
    return "Hello, " + names["fName"] + " " + names["sName"]

print(sayHello3(fName = "Joe", sName = "Blackkk"))
print()
#liambda - anonimus fanction and can run just one line of code
#(can be passes to another function, e.g. for some function data)

#7
def sayHello4(name: str) -> str:  
    print("Nihao, " + name)
sayHelloUa = lambda name:print("Privit, " +name)
#sayHello4("Eugene")
sayHelloUa("Eugene")

