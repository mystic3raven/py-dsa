class BitArray:
    def __init__(self, size):
        self.size = size
        self.array = 0

    def set_bit(self, position):
        """Set the bit at the specified position to 1."""
        if 0 <= position < self.size:
            self.array |= (1 << position)
            print(f"Set bit at position {position}.")
        else:
            raise IndexError("Bit position out of range.")

    def clear_bit(self, position):
        """Clear the bit at the specified position to 0."""
        if 0 <= position < self.size:
            self.array &= ~(1 << position)
            print(f"Cleared bit at position {position}.")
        else:
            raise IndexError("Bit position out of range.")

    def toggle_bit(self, position):
        """Toggle the bit at the specified position."""
        if 0 <= position < self.size:
            self.array ^= (1 << position)
            print(f"Toggled bit at position {position}.")
        else:
            raise IndexError("Bit position out of range.")

    def check_bit(self, position):
        """Check the value of the bit at the specified position."""
        if 0 <= position < self.size:
            result = (self.array & (1 << position)) != 0
            print(f"Bit at position {position} is {'set' if result else 'cleared'}.")
            return result
        else:
            raise IndexError("Bit position out of range.")

    def display(self):
        """Display the bit array."""
        bits = bin(self.array)[2:].zfill(self.size)
        print("BitArray:", bits[::-1])

# Usage
bit_array = BitArray(8)
bit_array.set_bit(1)
bit_array.set_bit(3)
bit_array.display()           # Output: BitArray: 00001010
bit_array.check_bit(3)        # Output: Bit at position 3 is set.
bit_array.clear_bit(1)
bit_array.toggle_bit(3)
bit_array.display()           # Output: BitArray: 00000000
