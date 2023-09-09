# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

    for i in name_list:
        j = i.strip("\n")
        with open("./Input/Letters/starting_letter.txt") as letter:
            new_letter = letter.read()
            name = new_letter.replace("[name]", f"{j}")
            with open(f"./Output/ReadyToSend/letter_for_{j}.txt", mode="w") as file:
                file.write(name)
