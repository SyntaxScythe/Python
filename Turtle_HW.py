def multiply_tuple(numbers):
    product = 1
    
    for num in numbers:
        product = product * num
    
    return product

test_tuple = (2, 3, 4, 5)
result = multiply_tuple(test_tuple)

print("The product is:", result)