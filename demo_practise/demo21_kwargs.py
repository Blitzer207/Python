'''
kwargs = key value arguments
'''


def m1(*args, **kwargs):
    print("the type of args is: ", type(args))
    print("the type of kwargs is: ", type(kwargs))


# dic_lei = {"name": "lei", "age": 23, "height": 182}


def someone(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)


someone(name="xiaoming", age="23", height= "180")
