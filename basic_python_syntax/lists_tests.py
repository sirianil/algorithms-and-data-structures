if __name__ == '__main__':
    mylist = [1,2,8,3,4,5]
    print(mylist[-1])

    newlist = [False] * 5
    print(newlist)

    mydict = {
        4: 5,
        1: 2,
        0: 1,
        5: 4
    }
    mylist = sorted(mydict.items(), key= lambda x: x[1])
    print(mylist)