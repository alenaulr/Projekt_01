"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alena Ulrichová
email: ulrichova.alena@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123'
}

separator = ('_' * 79)

####### PRIHLASENI UZIVATELE A UVITANI #######################################

username = input('Zadej přihlašovací jméno: ')
password = input('Zadej heslo: ')

print(separator)

if username in users and password == users[username]:
    print(f'Ahoj {username}, vítej v textovém analyzátoru!')
else:
    print('Přihlašovací údaje jsou nesprávné. Ukončuji program.')
    quit()

print(separator)

####### VYBER TEXTU ##########################################################

user_input = input('Zadej číslo textu k analýze (1-3): ')

print(separator)

if user_input.isdigit():
    index = int(user_input) - 1
    if 0 <= index < len(TEXTS):
        selected_text = TEXTS[index] #ulozi vybrany text pro dalsi analyzu
    else:
        print ('Zadané číslo není v rozsahu 1-3. Ukončuji program.')
        quit()
else: 
    print ('Vstup není číslo. Ukončuji program.')
    quit()

######## ANALYZA TEXTU #######################################################

words = selected_text.split()

capital_words = 0
uppercase_words = 0
lowercase_words = 0
number_count = 0
number_sum = 0

for word in words:
    if word.istitle():
        capital_words +=1
    if word.isupper():
        uppercase_words +=1
    if word.islower():
        lowercase_words +=1
    if word.isdigit():
        number_count += 1
        number_sum += int(word)

print(f'''
Počet slov v textu: {len(words)}.
Počet slov začínajících velkým písmenem: {capital_words}.
Počet slov psaných velkými písmeny: {uppercase_words}.
Počet slov psaných malými písmeny: {lowercase_words}.
Počet čísel v textu: {number_count}.
Součet všech čísel v textu: {number_sum}.
''')

print(separator)

####### SLOUPCOVY GRAF #######################################################

word_lengths = {}

for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print('\nDélka | Výskyt | Počet')
print(separator)

for length in sorted(word_lengths):
    count = word_lengths[length]
    stars = '*' * count
    print(f'{length:>3} | {stars:<20} | {count:>2}')
