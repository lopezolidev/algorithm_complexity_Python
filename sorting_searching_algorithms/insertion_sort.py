def insertion_sort(list):
    current_value = 0
    i = 1
    while i < len(list):
        current_value = list[i]
        current_position = i

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1
        
        list[current_position] = current_value
        i += 1