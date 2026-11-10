def add_int(text):
    is_int = False
    while not is_int:
        try:
            int_in = int(input(text))
            if int_in > 0:
                is_int = True
        except ValueError:
            print("this us not a legal choice ")
    return int_in

def add_str(text):
    legal_i = False
    while not legal_i:
        choice = input(text)
        if choice != "":
            legal_i = True
        else:
            print("enter a valeu")
    return choice

