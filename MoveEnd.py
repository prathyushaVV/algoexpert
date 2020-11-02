def move_element_at_end(array, num):
    i = 0
    j =len(array)-1
    while i < j :
        while i < j and array[j] == num:
            j -= 1
        if array[i] == num:
            array[i],array[j] = array[j], array[i]
        i += 1
    return array
array = [2,1,2,2,2,3,4,2]
print(move_element_at_end(array, 2))


#[4, 1, 2, 3, 2, 2, 2, 2]-this is the answer of the bove problem
