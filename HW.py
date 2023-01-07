# pg:80

# What is the simplest contradiction?
# to do something according to a condition

print("""Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, 
print ”OK;” otherwise, do not print anything.""")

p = int(input("Enter your number:"))


def number():
    if p > 100 or p < 0:
        print("NO")
    else:
        print("OK")


number()

print("""Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print ”OK;” 
otherwise, print ”Out of range."
""")

q = int(input("Enter your number:"))


def numeral():
    if q > 100 or q < 0:
        print("Out of range")
    else:
        print("OK")


numeral()


# 13. Write a Python program that allows a user to type in an English day of the week (Sunday, Monday, etc.). The program should print the Spanish equivalent, if possible.
# help

# 14. Consider the following Python code fragment:

print("Q:14 What will the code print if the variables i, j, and k have the following values?")
# (a) i is 3, j is 5, and k is 7
def heg(i,j,k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("(a) i =", i, " j =", j, " k =", k)
heg(3,5,7)
# (b) i is 3, j is 7, and k is 5
heg(3,7,5)
# (c) i is 5, j is 3, and k is 7
heg(5,3,7)
# (d) i is 5, j is 7, and k is 3
heg(5,7,3)
# (e) i is 7, j is 3, and k is 5
heg(7,3,5)
# (f) i is 7, j is 5, and k is 3
heg(7,5,3)
print("15. Consider the following Python program that prints one line of text:")
# (a) 3
def wow(val):
    if val < 10:
        if val != 5:
            print("wow ", end='')
        else:
            val += 1
    else:
        if val == 17:
            val += 10
        else:
            print("whoa ")
    print(val)
wow(3)
# (b) 21
wow(21)
# (c) 5
wow(5)
# (d) 17
wow(17)
print("""16. Write a Python program that requests five integer values from the user.
 It then prints the maximum and minimum values entered. If the user enters the values 3, 2, 5, 0, and 1, 
 the program would indicate that 5 is the maximum and 0 is the minimum. Your program should handle ties properly;for example, 
 if the user enters 2, 4 2, 3 and 3, the program should report 2 as the minimum and 4 as maximum.""")
a,b,c,d,e = (input("Enter 5 space separated numbers:")).split()
def vag():
    if a > b and a > c and a > d and a > e:
        print(a,"is biggest")
    elif b > a and b > c and b > d and b > e:
        print(b,"is biggest")
    elif c > a and a > b and a > d and a > e:
        print(c,"is biggest")
    elif d > a and d > b and d > c and a > e:
        print(d,"is biggest")
    else:
        print(e,"is biggest")
vag()

def vaj():
    if a < b and a < c and a < d and a < e:
        print(a,"is smallest")
    elif b < a and b < c and b < d and b < e:
        print(b,"is smallest")
    elif c < a and a < b and a < d and a < e:
        print(c,"is smallest")
    elif d < a and d < b and d < c and a < e:
        print(d,"is smallest")
    else:
        print(e,"is smallest")
vaj()

print("17. Write a Python program that requests five integer values from the user. It then prints one of two things: if any of the values entered are duplicates, it prints DUPLICATES; otherwise, it prints ALL UNIQUE")

l,w,x,y,z = (input("Enter 5 space seperated numbers:")).split()

def en():
    if l == w or l == x or l == y or l == z or w == x or w == y or w == z or x == y or x == z:
        print("DUPLICATES")
    else:
        print("ALL UNIQUE")
en()