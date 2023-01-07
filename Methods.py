
def addition():
    print(x+y,"Sum")
    #x added to y, if x and y are numbers
    #x concatenated to y, if x and y are strings

def subtraction():
    print(x-y,"difference")
    #x take away y, if x and y are numbers

def product():
    print(x*y,"product")
        #x times y, if x and y are numbers
        #x concatenated with itself y times, if x is a string and y is an integer y concatenated with itself x times, if y is a string and x is an integer
def division():
    print(x/y,"division")
    #x divided by y, if x and y are numbers
def integeral_divison():
    print(x // y,"Integral Division")
  #Integral part of x divided by y, if x and y are numbers

def remainder():
    print(x%y,"Remainder")
#Remainder of x divided by y, if x and y are numbers
def power():
    print(x ** y,"Power")
    #x raised to y power, if x and y are numbers
x = int(input("enter the first number:"))
y = int(input("enter the second number:"))

addition()
subtraction()
product()
division()
remainder()
power()
