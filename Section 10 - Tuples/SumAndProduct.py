# Write a function that calculates the sum and product
# of all elements in a tuple of numbers

def sum_product(input_tuple):
    size = len(input_tuple)
    sum_result =0
    product_result = 1
    for i in range(0, size,1):
        sum_result += input_tuple[i]
        product_result *= input_tuple[i]
        
    return sum_result, product_result    
        
        
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)