# input functions for specific data types

def input_int(prompt: str):
    '''Repeatedly prompts for input until an integer is entered.'''

    while True:
        value = input(prompt)

        try:
            validate_int = int(value)
            
        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue

        return validate_int

def input_str(prompt: str):
    '''Repeatedly prompts for input until something other than whitespace is entered.'''

    while True:
        value = input(prompt).strip()
            
        if value == '':
            print('Invalid input. Please enter something.')
            continue

        return value

# input functions for specific scenarios

def input_name(prompt: str):
    '''Repeatedly prompts for an input that is alphanumeric and a maximum of 16 characters."'''
    CHARACTER_LIMIT = 16
    
    while True:
        name = input_str(prompt)

        if not name.isalnum() or len(name) > CHARACTER_LIMIT:
            print("Invalid input. Name must be alphanumeric and a maximum of 16 characters.")
            continue

        return name

def input_selection(prompt: str, options: list):
    '''Repeatedly prompts for an input until the input matches a value from a list of options.'''

    while True:
        value = input_str(prompt).lower()

        if value not in options:
            print("Invalid input. Please enter one of the following options: " + str(options))
            continue
        
        return value
