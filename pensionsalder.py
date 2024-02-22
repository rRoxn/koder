
print('Välkommen till Pensionssimulatorn')

#Fråga användaren om namn
namn = input('Vad heter du? ')

#Fråga hur gammal
alder = int(input('Hur gammal är du? '))

#Pensionålder i Sverige
pensionålder = 65

#Beräkna år kvar
ar_kvar = pensionålder - alder

#Svara med
print (f'Hej {namn} du är {alder} år gammal och det är {ar_kvar} år till pensionen.')
