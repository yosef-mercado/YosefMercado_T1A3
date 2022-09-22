# "input_str" repeatedly prompts for input until something other than whitespace is entered.
def input_str(prompt):
    while True:
        value = input(prompt).strip()
            
        if value == '':
            print('Invalid input. Please enter something.')
            continue

        return value

# "input_int()" repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    while True:
        value = input(prompt)

        try:
            validate_int = int(value)
            
        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue

        return validate_int