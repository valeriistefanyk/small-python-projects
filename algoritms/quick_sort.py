def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [el for el in arr[1:] if el <= pivot]
    greater = [el for el in arr[1:] if el > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

    


if __name__ == "__main__":
    res = quick_sort([6, 4, 5, 6])
    print(res)