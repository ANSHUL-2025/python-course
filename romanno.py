class RomanConverter:
    # Mapping of Roman numerals
    _val_to_roman = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, number: int):
        """Initialize with an integer value"""
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number <= 0 or number > 3999:
            raise ValueError("Number must be between 1 and 3999.")
        self.number = number

    def to_roman(self) -> str:
        """Convert the integer to a Roman numeral"""
        n = self.number
        result = ""
        for value, symbol in self._val_to_roman:
            while n >= value:
                result += symbol
                n -= value
        return result

    @staticmethod
    def convert(number: int) -> str:
        """Static method to convert without creating an instance"""
        return RomanConverter(number).to_roman()


# Example usage:
num = RomanConverter(1987)
print(num.to_roman())   # MCMLXXXVII

print(RomanConverter.convert(2026))  # MMXXV
