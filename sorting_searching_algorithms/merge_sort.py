import random

def merge_sort(sequence):
    if len(sequence) > 1:
        half = len(sequence) // 2
        # obtaining the half of the list
        
        left = sequence[:half]
        right = sequence[half:]
        print("left: ", left, ' ' * 5, "right: ", right)
        # creating left and right subarrays

        merge_sort(left)
        merge_sort(right)
        # recursive call for each subarray

        i = 0
        j = 0
        # iterators for resorting trough both lists
        k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sequence[k] = right[j]
                j += 1
            else:
                sequence[k] = left[i]
                i += 1
            k += 1
        # copying the elements from left and right subarrays into the new sorted array

        while i < len(left):
            sequence[k] = left[i]
            i += 1
            k += 1
        # copying what's missing from left list into the sorted list

        while j < len(right):
            sequence[k] = right[j]
            j += 1
            k += 1
        # copying what's missing from right list into the sorted list

        print("left: ", left, ' ' * 5, "right: ", right)
        print(list)
        print(' ' * 50)
        return sequence

if __name__ == '__main__':
    list_size = int(input("Size of the list: "))

    sequence = [random.randint(0,100) for i in range(list_size)]
    print(sequence)
    print('-' * 20)

    sorted_list = merge_sort(sequence)
    print(sorted_list)

    