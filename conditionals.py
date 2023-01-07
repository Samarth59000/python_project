# inputs
i = int(input("Enter your number:"))
j = int(input("Enter your number:"))
k = int(input("Enter your number:"))
percentage = int(input("Enter your percentage:"))


# methods
def bigger():
    if i > j:
        print("I is bigger")
    else:
        print("J is bigger")


def percent():
    if percentage >= 40:
        print("pass")
        if percentage >= 90:
            print("Grade A")
        elif percentage >= 80:
            print("Grade B")
        elif percentage >= 70:
            print("Grade C")
        elif percentage >= 60:
            print("Grade D")
        elif percentage >= 50:
            print("Grade E")
        else:
            print("Grade F")

    else:
        print("fail")


def big():
    if j > i and j > k:
        print("J is greatest")
    elif i > j and i > k:
        print("I is the greatest")
    else:
        print("K is the greatest")


# main
bigger()
big()
percent()


value = eval(input("Please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
elif value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
else:
    print("Too large")
print('Done')

