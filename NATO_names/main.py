import pandas as pd

name_df = pd.read_csv('nato_phonetic_alphabet.csv')

# print(name_df)

name_dict = {row.letter:row.code for (index, row) in name_df.iterrows()}
# print(name_dict)


def generate_phonetic():
    user_word = input('Enter a word: ')

    try:
        user_list = [name_dict[key] for key in user_word.upper()]


    except KeyError:
        print('Sorry, only letters in the alphabets please')
        generate_phonetic()

    else:
        print(user_list)
        end_of_program = True

generate_phonetic()
