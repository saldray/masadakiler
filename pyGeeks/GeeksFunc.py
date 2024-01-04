# def fun():
#     print("Welcome to GFG")

# fun()


# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2

#     return num3

# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} result {ans}.")

# #prime numbers asal sayılar

# def is_prime(n):
#     if n in [2, 3]:
#         return True
#     if (n == 1) or (n % 2 == 0):
#         return False
#     r = 3
#     while r * r <= n:
#         if n % r == 0:
#             return False
#         r += 2
#     return True
# print(is_prime(78), is_prime(79))



# # A simple Python function to check
# # whether x is even or odd

# def evenOdd(x):
#     if(x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# evenOdd(2)
# evenOdd(3)


# # Python program to demonstrate
# # default arguments
# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)


# # Python program to demonstrate Keyword Arguments
# def student(firstname, lastname):
#     print(firstname, lastname)


# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')


# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is", age)


# # You will get corret output because
# # arguments is given in order
# print("Case-1:")
# nameAge("Suraj", 27)
# # You will get incorret output because
# # arguments is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")

# # Variable length non-keywords arguments

# # Python program to illustrate
# # *args for variable number of arguments
# def myFun(*argv):
#     for arg in argv:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))

# myFun(first='Geeks', mid='for', last='Geeks')

# # conputer geek = bilgisayar meraklısı


# def evenOdd(x):
#     """Function to check if the number is even or odd"""
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# print(evenOdd.__doc__)



# Python program to
# demonstrate accessing of
# variable of nested functions

def f1():
    s = 'I love GeeksGeeks'

    def f2():
        print(s)

    f2()

f1()

# https://www.geeksforgeeks.org/python-functions/?ref=lbp

# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))


# Here x is a nex reference to same list lst
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]

myFun(lst)
print(lst)


def myFun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Note that x is not modified
# after function call.
x = 10
myFun(x)
print(x)
