PLACEHOLDER = "[name]"


with open("/Users/melih/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as file_invited_names:
    invited_names = file_invited_names.readlines()                # list
    #print(invited_names)

with open("/Users/melih/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file_starting_letter:
    starting_letter = file_starting_letter.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = starting_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/melih/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


