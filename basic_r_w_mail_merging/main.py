#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open('./Input/Letters/starting_letter.txt', mode="r") as file:
    content = file.readlines()

with open('./Input/Names/invited_names.txt', mode="r") as name_file:
    names = name_file.readlines()
name_list = [name.strip() for name in names]


# for making a file first and then appending the text.
for name in name_list:
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as mail:
        mail.write(f"Dear {name},\n")

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='a') as mails:
        for content_line in content[1:]:
            mails.write(f"{content_line}")
