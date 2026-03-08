def contains_duplicate(array):
    nums_set = set()
    for i in range(len(array)):
        if array[i] in nums_set:
            return True
        nums_set.add(array[i])

    return False


def main():
    array = [1, 10, 11, 14, 17, 20, 1]
    result = contains_duplicate(array)
    print(result)

if __name__ == '__main__':
    main()