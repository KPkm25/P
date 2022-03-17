import math 
def jump_search(list_of_numbers, key): 
    list_length = len(list_of_numbers) 
    jump = int(math.sqrt(list_length)) 
    left, right = 0, 0 
    while left < list_length and list_of_numbers[left] <= key:
        right = min(list_length - 1, left + jump) 
        if list_of_numbers[left] <= key <= list_of_numbers[right]: 
            break 
        left += jump 
    if left >= list_length or list_of_numbers[left] > key: 
         return -1 
    right = min(list_length - 1, right) 
    i = left 
    while i <= right and list_of_numbers[i] <= key: 
        if list_of_numbers[i] == key: 
            return i 
        i += 1 
    return -1 
def user_input(): 
    list_of_numbers = list() 
    total_elements = input("Enter a list of numbers in ascending order with  space between each other: ").split() 
    for each_element in range(len(total_elements)): 
        list_of_numbers.append(int(total_elements[each_element])) 
    key = int(input("Enter the Key number to search: ")) 
    index = jump_search(list_of_numbers, key) 
    if index == -1: 
        print("Entered key is not present") 
    else: 
        print(f"Key number {key} is found in Position {index + 1}") 
if __name__ == "__main__": 
 user_input()
