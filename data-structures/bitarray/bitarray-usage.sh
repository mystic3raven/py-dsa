from bitarray import bitarray

# Create a bit array with a specified size
size = 8
bit_arr = bitarray(size)
bit_arr.setall(0)  # Initialize all bits to 0

# Set specific bits
bit_arr[1] = 1
bit_arr[3] = 1

# Display the bit array
print("BitArray:", bit_arr)  # Output: BitArray: bitarray('01001000')

# Check specific bits
print("Bit at position 3 is", "set" if bit_arr[3] else "cleared")  # Output: set

# Toggle a bit
bit_arr[3] = not bit_arr[3]

# Clear a bit
bit_arr[1] = 0

# Display the updated bit array
print("BitArray:", bit_arr)  # Output: BitArray: bitarray('00000000')
