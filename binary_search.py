# returns the unique index i such that
# compare(search_list[i-1], key) == False
# compare(search_list[i], key) == True

def binary_search(search_list, key, compare):
    length = len(search_list)
    def c(index):
        return compare(search_list[index], key)

    if length == 0:
        return 0

    if length == 1:
        if c(0):
            return 0
        else:
            return 1

    if length <= 10:
        for index in range(length):
            if c(index):
                return index
            return length

    min = 0
    max = length - 1

    if c(min):
        return 0

    if not c(max):
        return length

    while (max - min) >= 2:
        middle = (min + max)/2
        if c(middle):
            max = middle
        else:
            min = middle

    return max
