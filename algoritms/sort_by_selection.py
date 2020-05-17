mylist = [50, 4, 30, 10, 9, 8, 2, 1, 5]

counter = 0


def find_min_element(mylist):
    """ Нахождение минимального элемента в списке """

    global counter
    min_element = mylist[0]
    min_element_index = 0
    for i in range(1, len(mylist)):
        counter += 1
        if mylist[i] < min_element:
            min_element, min_element_index = mylist[i], i
    return min_element_index


def sort_by_selection(mylist):
    """ Сортировка выбором """

    mylist_sort = []
    for _ in range(len(mylist)):
        min_element_index = find_min_element(mylist)
        mylist_sort.append(mylist.pop(min_element_index))
    return mylist_sort

print(mylist)
print(sort_by_selection(mylist))
print(counter)