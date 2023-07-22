import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(nato_dict)

try:
    user_input = input("Type a name: ").upper()
    letters = [nato_dict[letter] for letter in user_input if letter in nato_dict]


print(letters)
