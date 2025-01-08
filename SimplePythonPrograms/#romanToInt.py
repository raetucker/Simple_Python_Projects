#romanToInt.py
#This program accepts a user input  to convert a Roman numeral to an integer

def is_valid_roman(s):
    # Define valid Roman numeral characters
    valid_characters = "IVXLCDM"
    
    # Loop through each character in the input string
    for char in s:
        if char not in valid_characters:
            return False  # If any character is not valid, return False
    
    return True  # If all characters are valid, return True

def romanToInt(s):
    # Define a dictionary for Roman numerals and their integer values
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize a variable to store the result
    result = 0
    
    # Loop through the string to process the Roman numerals
    for i in range(len(s)):
        # Get the value of the current Roman numeral
        current_value = roman_numerals[s[i]]
        
        # Check if the current value is less than the next value (subtraction case)
        if i + 1 < len(s) and current_value < roman_numerals[s[i + 1]]:
            # Subtract the current value (this handles cases like IV, IX, etc.)
            result -= current_value
        else:
            # Otherwise, add the current value to the result
            result += current_value
    
    return result

def main():
    # Get user input for the Roman numeral and convert to uppercase
    user_input = input("Enter a Roman numeral: ").upper()  # Convert to uppercase to ensure uniformity

    # Validate the user input
    if not is_valid_roman(user_input):
        print("Invalid Roman numeral. Please enter a valid Roman numeral (uppercase).")
    else:
        # If valid, convert to integer and print the result
        integer_value = romanToInt(user_input)
        print(f"The integer value of {user_input} is {integer_value}.")

# Call the main function
main()