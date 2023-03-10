import pandas as pd  

df = pd.read_csv(r"C:\Users\utsha\OneDrive\Desktop\my learning\python fresh start\code\day44\nato phonetic updated\nato_phonetic_alphabet.csv")

nato_dict = {row.letter : row.code for (index,row) in df.iterrows()}

def entry():
    name = input("Enter any word : ").upper()
    name_list = list(name)
    try:
        nato_list = [nato_dict[letter] for letter in name_list]
    except KeyError:
        print("Numbers are not allowed enter alphabet")
        entry()
    else:
        print(nato_list)
entry()