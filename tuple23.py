def product_of_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage
numbers = (2, 3, 4, 5)
result = product_of_tuple(numbers)
print("Tuple:", numbers)
print("Product of tuple elements:", result)
