letter = '''
Dear Divyanshu,
You are selected!
11-04-2024'''

print(letter)

# replce things
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Mayank Tailor").replace("<|Date|>" , "11-04-2024"))