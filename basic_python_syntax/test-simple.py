def simple_test():
    array_tuples = [(1,2,3),(2,3,4),(4,5,6)]

    for x,y,z in array_tuples:
        print(x)
        print(y)
        print(z)

    a = True
    b = None

    if (b and a):
        print("this works")

if __name__ == '__main__':
    simple_test()