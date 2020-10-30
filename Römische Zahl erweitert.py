roman_number = input("Bitte geben sie eine Römische Zahl ein: ")

decimal = 0
roman_digits = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }


previous_value = 0
for char in roman_number:
    if char in roman_digits:
        if roman_digits[char] > previous_value:
            decimal -= previous_value
        else:
            decimal += previous_value
        previous_value = roman_digits[char]
    else:
        print("keine Römische Zahl")
        
print("Dezimal: " + str(decimal))
        