# Write a function that takes a tuple and a value,
# and returns a new tuple with the value inserted
# at the beginning of the original tuple.

def insert_value_front(input_tuple, value_to_insert):
    input_tuple = list(input_tuple)
    input_tuple.insert(0, value_to_insert)
    input_tuple = tuple(input_tuple)
    
    return input_tuple
    # return (value_to_insert,) + input_tuple - comma after the value is necessary to create a single-element tuple
    # linear time complexity O(n), where n is the length of the input tuple, as it creates a new tuple by copying the elements from the original tuple. The space complexity is also O(n) because it creates a new tuple with n+1 elements.


input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple) 