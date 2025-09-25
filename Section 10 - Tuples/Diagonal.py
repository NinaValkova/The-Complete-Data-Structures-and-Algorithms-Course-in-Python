# Create a function that takes a tuple of tuples and returns a tuple
# containing the diagonal elements of the input.


def get_diagonal(tup):
    size = len(tup)
    
    tup_diagonal = []
    for row_index in range(0, size):
        for col_index in range(0, size):
            if col_index == row_index:
                tup_diagonal.append(tup[row_index][col_index])
    
    return tuple(tup_diagonal)   
    # return tuple(input_tuple[i][i] for i in range(len(input_tuple)))
    # The time complexity is O(n), where n is the length of the input tuple
    # because it iterates through the indices once. The space complexity is O(n)
    # because it creates a new tuple containing the diagonal elements,
    # which has a length equal to the length of the input tuple.

     
                

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple) 