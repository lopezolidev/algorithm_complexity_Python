import random

def linear_search(list, target):
    match = False
    counter = 0

    for element in list: # O(n) ← the worst case this is the time complexity of this algorithm
        counter += 1
        print(f"Counter {counter}")
        if element == target:
            match = True
            break
    
    return match

if __name__ == '__main__':
    list_size = int(input("Which size would you like the list? "))
    target = int(input("Which number would you like to find? "))

    sequence = [random.randint(0,100) for i in range(list_size)]

    found = linear_search(sequence, target)

    print(sequence)
    print(f'The element {target} was {"found" if found else "not found"} in the list')