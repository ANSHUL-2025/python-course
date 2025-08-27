# Program to generate squares of numbers in a range 
# and separate them into odd and even values

# Taking range input from user
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# Generate list of squares
squares = [num**2 for num in range(start, end+1)]

# Separate odd and even squares
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Display results
print(f"\nSquares of numbers from {start} to {end}: {squares}")
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")
