import random
print('Välkomna till bingospelet')

def spela_bingo():
    # Användaren skriver in 10 tal
    print("Skriv in 10 tal mellan 0-50:")
    inskrivna_tal = []
    for i in range(10):
        inskrivet_tal = int(input(f"Skriv in tal {i + 1}: "))
        inskrivna_tal.append(inskrivet_tal)

    # Slumpa tio tal och lagra dem i en vektor
    slumpade_tal = []
    for _ in range(10):
        slumpade_tal.append(random.randint(1, 50))  # Antalet bollar i en bingo är 1-50

    poang = 0

    # Jämför slumpade tal med inskrivna tal
    bingo_tal = []
    for tal in slumpade_tal:
        if tal in inskrivna_tal:
            poang += 1
            inskrivna_tal.remove(tal)
            bingo_tal.append(tal)
        else:
            print(tal, end=' ')

    # Skriv ut alla bingon och poäng på samma rad
    print("\nBingo:", bingo_tal)
    print("Dina poäng:", poang)

# Huvudloop
while True:
    spela_bingo()
    svar = input("Vill du spela igen? (ja/nej): ")
    if svar.lower() != 'ja':
        break

print("Tack för att du spelade Bingo!")
