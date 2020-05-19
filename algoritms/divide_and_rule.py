""" 
Принцип разделяй и властвуй: 
    1. Определить простейший случай как базовый
    2. Придумать как свести задачу к базовому случаю
"""

def calculate(height, weight):
    if weight > height:
        height, weight = weight, height
    
    if height % weight == 0:
        return weight

    div = height // weight
    height = height - (weight * div)
    return calculate(height, weight)


def my_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + my_sum(arr)


if __name__ == "__main__":
    res = calculate(1680, 640)
    print(res)
    arr = [1, 2, 4, 5, 6]
    print(my_sum(arr))