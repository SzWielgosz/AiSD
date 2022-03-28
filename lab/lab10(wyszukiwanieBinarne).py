def binarySearch(numbers, value: int): #zlozonosc log(n)
    p = 0
    q = len(numbers)
    while p <= q:
        middle = int((p + q) / 2)
        if numbers[middle] == value:
            return middle, True

        elif numbers[middle] < value:
            p += 1

        elif numbers[middle] > value:
            q -= 1

    return -1, False


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 12]
print(binarySearch(li, 10))