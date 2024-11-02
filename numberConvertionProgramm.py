def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal number."""
    return int(binary_str, 2)

def octal_to_decimal(octal_str):
    """Converts an octal string to a decimal number."""
    return int(octal_str, 8)

def hexadecimal_to_decimal(hex_str):
    """Converts a hexadecimal string to a decimal number."""
    return int(hex_str, 16)

def decimal_to_binary(decimal_num):
    """Converts a decimal number to a binary string."""
    return bin(decimal_num)[2:]

# Function to display menu and perform conversions
def number_conversion():
    print("Choose a conversion type:")
    print("1. Binary to Decimal")
    print("2. Octal to Decimal")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Binary")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        binary_str = input("Enter a binary number: ")
        result = binary_to_decimal(binary_str)
        print(f"Binary {binary_str} in decimal is {result}")

    elif choice == '2':
        octal_str = input("Enter an octal number: ")
        result = octal_to_decimal(octal_str)
        print(f"Octal {octal_str} in decimal is {result}")

    elif choice == '3':
        hex_str = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_decimal(hex_str)
        print(f"Hexadecimal {hex_str} in decimal is {result}")

    elif choice == '4':
        decimal_num = int(input("Enter a decimal number: "))
        result = decimal_to_binary(decimal_num)
        print(f"Decimal {decimal_num} in binary is {result}")

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
number_conversion()
