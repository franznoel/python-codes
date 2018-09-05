def testing_kwargs(**kwargs):
    # print the dictionary
    print(kwargs)

    # print each kwarg items
    for key, value in kwargs.items():
        print("{0} {1}".format(key,value))

testing_kwargs(firstname="John",lastname="Smith",age="45")

