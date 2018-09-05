fruits = ['apple', 'banana', 'grapes', 'pear']

# Using enumerate print
print("Using enumerate, then print:")
for c, value in enumerate(fruits, 1):
    print(c, value)

# Using enumerate to create list of tuples
print("\n Using enumerate to create list of tuples")
fruit_list = list(enumerate(fruits, 1))
print(fruit_list)

# Display the list of fruits
for key, value in fruit_list:
    print (key, value)

