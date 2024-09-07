import random 

def binary_search(list, start, end, target, counter):
    if start > end:
        return False
    
    counter += 1
    print(f"Counter: {counter}, looking for {target} between {list[start]} and {list[end - 1]}")
    half = (start + end) // 2

    if list[half] == target:
        return True
    
    if list[half] < target:
        return binary_search(list, half + 1, end, target, counter)

    if list[half] > target:
        return binary_search(list, start, half - 1, target, counter)    

def iterative_binary_search(list, target):
    i = 1
    j = len(list) - 1
    while i < j:
        m = (i + j) // 2
        if target > list[m]:
            i += 1
        else: 
            j = m
    if target == list[i]:
        return True
    return False

if __name__ == '__main__':
    list_size = int(input("Which size would you like the list? "))
    target = int(input("Which number would you like to find? "))

    sequence = sorted([random.randint(0,100) for i in range(list_size)])

    counter = 0

    found = iterative_binary_search(sequence, target)

    print(sequence)
    print(f'The element {target} was {"found" if found else "not found"} in the list')