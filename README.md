# Number_convertion
#It is used to convey the Number from one form to the other form........ It converts  1 ] Binary to Decimal             #2 ] Octal to Decimal             3 ] Hexadecimal to Decimal             4 ] Decimal to Binary
#code : 


def binary_to_decimal(binary):
    decimal = 0
    power = 0
    integer_part, fractional_part = str(binary).split('.')
    for digit in reversed(integer_part):
        decimal += int(digit) * (2 ** power)
        power += 1

    if fractional_part:
        power = -1
        for digit in fractional_part:
            decimal += int(digit) * (2 ** power)
            power -= 1

    return decimal


def octal_to_decimal(octal):
    decimal = 0
    power = 0
    integer_part, fractional_part = str(octal).split('.')
    for digit in reversed(integer_part):
        decimal += int(digit) * (8 ** power)
        power += 1

    if fractional_part:
        power = -1
        for digit in fractional_part:
            decimal += int(digit) * (8 ** power)
            power -= 1

    return decimal


def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    integer_part, fractional_part = str(hexadecimal).split('.')
    for digit in reversed(integer_part):
        decimal += hex_dict[digit.upper()] * (16 ** power)
        power += 1

    if fractional_part:
        power = -1
        for digit in fractional_part:
            decimal += hex_dict[digit.upper()] * (16 ** power)
            power -= 1

    return decimal


def decimal_to_binary(decimal):
    integer_part = int(decimal)
    fractional_part = decimal - integer_part

    binary = ""
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part //= 2

    if fractional_part > 0:
        binary += "."

        max_precision = 8  # Set the maximum precision for the fractional part
        precision = 0
        while fractional_part > 0 and precision < max_precision:
            fractional_part *= 2
            bit = int(fractional_part)
            binary += str(bit)
            fractional_part -= bit
            precision += 1

    return binary
print(''' please select the method which you want to convert : 
      (# please select only number )
            1 ] Binary to Decimal
            2 ] Octal to Decimal
            3 ] Hexadecimal to Decimal
            4 ] Decimal to Binary
            ''')
x=int(input('ENTER THE NUMBER OVER HERE : '))
if(x==1 or 2 or 3 or 4):
    if(x==1):
        binary_number = input('enter the binary number : ')
        decimal_number = binary_to_decimal(binary_number)
        print(f"Binary: {binary_number} -> Decimal: {decimal_number}")
    if(x==2):
        octal_number = input('enter the octal number : ')
        decimal_number = octal_to_decimal(octal_number)
        print(f"Octal: {octal_number} -> Decimal: {decimal_number}")
    if(x==3):
        hexadecimal_number = input('enter the hexa decimal number : ')
        decimal_number = hexadecimal_to_decimal(hexadecimal_number)
        print(f"Hexadecimal: {hexadecimal_number} -> Decimal: {decimal_number}")
    if(x==4):
        decimal_number = float(input("Enter the decimal number : "))
        binary_number = decimal_to_binary(decimal_number)
        print(f"Decimal: {decimal_number} -> Binary: {binary_number}")

else:
    print('You did not give the right choice')
