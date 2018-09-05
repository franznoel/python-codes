categories = ["mammals","reptiles","insects"]
animals = ["cow", "dog", "viper", "python", "bee","fly"]

print({ y[1] : { x[1] for x in enumerate(animals) if x[0] in where[y[0]] } for y in enumerate(categories) })

