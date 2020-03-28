
'''
what is *args  tuple type

args = arguments  * == all
'''


# def add(num1,num2):
#     print(num1+num2)
#
# add(1,2)

# def add(*args):
#     print(sum(args))
#
# add(1,2)

def add(*args):
    for name in args:
        print('i love ', name)

print('xiaoming','wanger','wangba','lisi')