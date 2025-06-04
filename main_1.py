# Úvodní hlavička
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Rattay
email: rattyy@seznam.cz
"""
# Texty
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
# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Prihlaseni

username = input("Zadejte prihlasovaci jmeno: ")
password = input("Zadejte heslo: ")

if username in users and users[username] == password:
    print(f"Ahoj {username}, vítej v textovém analyzátoru!")
else:
    print("Nesprávné uživatelské jméno nebo heslo. Program se vypne!")   
    exit()

print("Máme 3 texty k analýze.")  

# Analýza textu 

volba = input("Zadejte číslo textu, který chcete analyzovat (1-3): ")

if not volba.isdigit():
    print("Zadejte číslo! Program se vypne!")
    exit()

volba = int(volba)

if volba < 1 or volba > len(TEXTS):
    print("Zadané číslo není v daném rozsahu, program se vypne!")  
    exit()  

vybrany_text = TEXTS[volba - 1] 
slova = vybrany_text.split()   

pocet_slov = len(slova)
pocet_slov_zacinajici_velkym_pismenem = 0
pocet_slov_psanymi_velkymi_pismeny = 0
pocet_slov_psanymi_malymi_pismeny = 0
pocet_cisel = 0 
suma_vsech_cisel = 0

for pocet in slova:
    pocet = pocet.strip(".,!?()[]\"")

    if pocet[0].isupper():
        pocet_slov_zacinajici_velkym_pismenem += 1
    if pocet.isupper():
        pocet_slov_psanymi_velkymi_pismeny += 1
    if pocet.islower():
        pocet_slov_psanymi_malymi_pismeny += 1
    if pocet.isdigit():
        pocet_cisel += 1 
        suma_vsech_cisel += int(pocet)

# Výstup + graf

if volba in range(1, 4):
    print(
        f"V textu je {pocet_slov} slov.\n"
        f"V textu je {pocet_slov_zacinajici_velkym_pismenem} slov začínajícím velkým písmenem.\n"
        f"V textu je {pocet_slov_psanymi_velkymi_pismeny} slov psaných velkými písmeny.\n"
        f"V textu je {pocet_slov_psanymi_malymi_pismeny} slov psaných malými písmeny.\n"
        f"V textu je {pocet_cisel} čísel.\n"
        f"V textu je suma vsech čísel {suma_vsech_cisel}.\n")

delky_slov = {}

for slovo in slova:
    slovo = slovo.strip(".,!?()[]\"")
    delka = len(slovo)
    if delka == 0:
        continue
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1

print("DÉLKA | POČET | GRAF")
print("---------------------")

for delka in sorted(delky_slov):
    pocet = delky_slov[delka]
    graf = '*' * pocet
    print(f"{delka:>5} | {pocet:>5} | {graf}")