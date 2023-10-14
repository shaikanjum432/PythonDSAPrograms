def binary_search(input_array, value):
    final_array = input_array
    while len(input_array) >=1 :
        size_of_list = len(input_array)
        
        if(size_of_list %2) != 0:
            middle_element = input_array[size_of_list//2]
        else:
            middle_element = input_array[(size_of_list//2)-1]
        
        if(value == middle_element):
            return final_array.index(middle_element)
        elif(value < middle_element):
            input_array = input_array[:(input_array.index(middle_element))]
        elif(value > middle_element):
            input_array = input_array[((input_array.index(middle_element))+1):]

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))