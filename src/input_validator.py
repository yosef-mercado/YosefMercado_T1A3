def input_str(prompt):
    '''"input_str" repeatedly prompts for input until something other than whitespace is entered.'''

    while True:
        value = input(prompt).strip()
            
        if value == '':
            print('Invalid input. Please enter something.')
            continue

        return value

def input_int(prompt):
    '''"input_int()" repeatedly prompts for input until an integer is entered.'''

    while True:
        value = input(prompt)

        try:
            validate_int = int(value)
            
        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue

        return validate_int

def input_selection(options: list):
    '''"input_selection()" repeatedly prompts for an input until the input matches a value in a list of valid values.'''

    while True:
        value = input_str(str(options) + ": ")

        if value.lower() not in options:
            print("Invalid input. Please enter one of the following options: " + str(options))
            continue
        
        return value