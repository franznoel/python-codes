def testing_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} {1}".format(key,value))

testing_kwargs(firstname="John",lastname="Smith",age="45")