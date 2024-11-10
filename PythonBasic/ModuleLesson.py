#oblast vidimosti: glabal and local (in the function)
x = 1 #global var 
def new_func():
    x = 10000 #priority is var v oblast vidimosti local in funct
    # global a a = 100 print (a)
    print(x)
new_func()
print(x)

# IMPORT MODULES
import module #from module import cars
# from module import cars - only cars var
# import cars as cars1
print(module.cars[2])
print(module.cars)
print(dir(module)) #shows vars in the module