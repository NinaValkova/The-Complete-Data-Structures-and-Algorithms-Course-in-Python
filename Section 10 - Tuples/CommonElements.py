# Write a function that takes two tuples and returns
# a tuple containing the common elements of the input tuples.


def common_elements(tuple1, tuple2):
    elements = []
    
    size_tup1 = len(tuple1)
    size_tup2 = len(tuple2)
    for i in range(size_tup1):
        for j in range(size_tup2):
            if tuple1[i] == tuple2[j]:
                elements.append(tuple1[i])
            
    return tuple(elements)   

    # return tuple(x for x in tuple1 if x in tuple2)
    
    # return tuple(set(tuple1) & set(tuple2))
    # This line creates two sets from the input tuples using the set() constructor,
    # and then computes the set intersection using the & operator.
    # The time complexity of creating each set is O(n),
    # where n is the length of the input tuple.
    # The time complexity of computing the set intersection is O(min(n,m)),
    # where m is the length of the second input tuple.
    # Since the two input tuples are of equal length,
    # the overall time complexity of the function is O(n).
    # The space complexity is also O(n)
    # because the size of the resulting set will be no
    # larger than the size of the smaller of the two input tuples.

        
            
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple) 