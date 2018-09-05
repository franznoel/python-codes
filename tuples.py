def returnValues(z):
    results = [(x, y)
        for x in range(z)
        for y in range(z)
        if x + y == 5
        if x > y]

    return results

print(returnValues(10))