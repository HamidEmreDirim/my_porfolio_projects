
with open("data.txt", encoding="UTF8") as f:
    data = f.read()

data = data.split()

current_alphabet = data[: :2]
mors_alphabet = data[1: :2]

data_map = dict(zip(current_alphabet, mors_alphabet))

users_input = input("Type your sentence:  ")

morse_text = ""

index_counter = 0
space_reset = False

for character in users_input:
    
    

    if character == " " and space_reset == True:  
        pass


    elif character == " " and space_reset == False:
        morse_text += " / "
        space_reset = True


    else:
        space_reset = False

        if index_counter == 0:   
            morse_text += data_map[character.upper()]
        else:
            morse_text += " "
            morse_text += data_map[character.upper()]


    index_counter += 1


print(f"Your morse text is: '{morse_text}' .")