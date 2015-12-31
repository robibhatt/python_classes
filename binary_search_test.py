import binary_search

search_list = range(1000)
def compare(a,b):
    return (b < a)

for index in range(1000):
    assert binary_search.binary_search(search_list, index, compare) == (index + 1)

print "yay passed"
