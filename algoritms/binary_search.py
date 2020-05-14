

def binary_search(nums, element):
    low = 0
    high = len(nums) - 1
    nums.sort()

    num_steps = 0
    print(nums)
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        num_steps += 1
        if guess == element:
            return mid, num_steps    
        if guess < element:
            low = mid + 1
        else:
            high = mid - 1
    return None, num_steps


if __name__ == "__main__":

    nums = [1, 2, 4, 7, 3, 2, 9, 3, 6, 0, 11, 2, 22, 3243, 2, 1, 67]
    
    element = 2
    position, steps = binary_search(nums, element)
    print(f"nums[{position}] = {element}. Найдено за {steps} шагов")
    
    element = 67
    position, steps = binary_search(nums, element)
    print(f"nums[{position}] = {element}. Найдено за {steps} шагов")