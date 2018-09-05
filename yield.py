print("Using yield on a simple loop:")
# using yield
def generator_function():
    for i in range(10):
        yield i

for i in generator_function():
    print (i)


# fibonacci generator:
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print("\nFibonacci:")

for i in fibon(25):
    print(i)


# Using next Python function after generation
print("\nUsing next:")

def generator_function():
    for i in range(4):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))

#Using next in string
print("\nUsing next in string:")
my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))