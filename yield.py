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