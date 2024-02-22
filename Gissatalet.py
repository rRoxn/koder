import random
# Hälsa välkommna och förklara regler
print("Välkommen till Gissa Talet! ")
print("Målet är att gissa ett slumpmässigt tal mellan 1 och 100, Man har 10 försök på sig.")
print("Du har 3 spelomgångar på dig. Lycka till!\n")
# Funktion för att spela en spelomgång
def spela_omgang():
  # Slumpa ett tal mellan 1 och 100
  hemligt_tal = random.randint(1, 100)

  # Lista för att spara gissningar
  gissningar = []

  # Räknare för gissningar
  gissningar_antal = 0


  # Loopa tills användaren gissar rätt eller når 10 gissningar
  # Fråga användare om gissning
  # Kontrollera om gissning används
  # Spara gissinig i lista
  # Visa lista för användare
  # Kontrollera om gissning var rätt. Om rätt printa grattis och börja om. Om fel printa ge tips om högt eller lågt
  # Öka gissningsräknaren
  for _ in range(10):
    gissning = int(input("Gissa ett tal: "))

    if gissning in gissningar:
        print("Du har redan gissat på", gissning, ". Gissa en ny siffra!")
        continue

    gissningar.append(gissning)
    print("Dina gissningar hittills:", gissningar)

    if gissning == hemligt_tal:
        print("Grattis! Du gissade rätt på", gissningar_antal + 1, "försök!")
        break
    elif gissning > hemligt_tal:
        print("Ditt tal är för högt. Hemliga talet är lägre.")
    else:
        print("Ditt tal är för lågt. Hemliga talet är högre.")

    gissningar_antal += 1

  # Visa meddelande om användaren inte gissar rätt efter 10 försök.
  if gissningar_antal == 10:
    print("Du har inte gissat rätt efter 10 försök. Hemliga talet var", hemligt_tal)
    return "Klarade ej"
  else:
    return gissningar_antal

# Huvudfunktion
 # Lista för att spara poäng
 # Lista för att spara alla spelomgångar
 # Bästa försök
 # Spela 3 spelomgångar
def main():

  poang = []


  spelomgangar = []


  basta_forsok = 10


  for i in range(3):
    print(f"Omgång {i + 1}:")
    resultat = spela_omgang()
    spelomgangar.append((i + 1, resultat))

    if isinstance(resultat, str):
      print(resultat)
    else:
      poang.append(resultat)
      # Uppdatera bästa försök
      if resultat < basta_forsok:
        basta_forsok = resultat

  # Visa poäng
  print("Dina poäng:")
  for i, poang in enumerate(poang):
    print(f"Omgång {i + 1}: {poang} gissningar")

  # Visa bästa försök
  print(f"Bästa försök: {basta_forsok} gissningar")

  # Visa alla spelomgångar
  print("Alla spelomgångar:")
  for i, resultat in spelomgangar:
    if isinstance(resultat, str):
      print(f"Omgång {i}: {resultat}")
    else:
      print(f"Omgång {i}: {resultat} gissningar")

  # Fråga om användaren vill spela igen
  svar = input("Vill du spela igen? Skriv 'ja' eller 'nej': ").strip().lower()
  while svar not in ("ja", "nej"):
    svar = input("Felaktigt svar. Skriv 'ja' eller 'nej': ").strip().lower()

  # Spela igen om användaren skriver "ja"
  if svar == "ja":
    main()

  # Tacka användaren om de säger nej
  if svar == "nej":
    print("Tack för att du spelade!")

# Starta huvudfunktionen
if __name__ == "__main__":
  main()



 
