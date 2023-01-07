x = 5

def func():
    x = 7
    print (x,"inside func")
def function():
    x = 9
    print(x, "inside function")
    return x

print(x, "outside function")
func()
print ("outside func:",x)
x = function()

print ("outside func:",x)