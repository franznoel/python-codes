# using lambda to add
print("Result in using lambdas x+y")
add = lambda x, y: x + y
print(add(5,10))

# using Lambda and map
print("\nUsing lambda with map:")
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print (squared)

# using lambda and key
print("\nUsing lambda with key")
a = [(1, 2), (4, 1), (9, 10), (13, -3)]

# print after sorting by second key value
a.sort(key=lambda x: x[1])
print (a)

# print after sorting by first key value
a.sort(key=lambda x: x[0])
print (a)
