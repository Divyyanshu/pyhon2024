# 1. Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!

hindi_to_english = {
    "Namaste": "Hello",
    "Dhanyavaad": "Thank you",
    "Sapna": "Dream",
    "Pyar": "Love",
    "Khushi": "Happiness",
    "Dost": "Friend",
    "Parivar": "Family",
    "Gyaan": "Knowledge",
    "Shakti": "Strength",
    "Sahas": "Courage"
}

word_input = input("enter your word : ")
print(hindi_to_english[word_input])