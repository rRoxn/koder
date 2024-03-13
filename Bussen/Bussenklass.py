"""Detta är koden till bussen, detta är klassen med meny och funktionerna till denna simulation"""
import random #Importera random funktion för 7 val möjligheten.


class Buss:
    
    passagerare = []  # Lista för att spara passagerare.
    antal_passagerare = 0  # En variabel för att spara antal passagare. 

    def __init__(self):
        self.passagerare  = []
        self.antal_passagerare = 0

    def run(self):
        print("Välkomna till busssimulatorn")
        # Meny med olika val för användaren.
        while True:
            print("=========================== ")
            print("Välj ett av alternativen:")
            print(" ======================= ")
            print("1. Lägg till passagerare.")
            print("2. Skriv ut alla passagerare.")
            print("3. Beräkna den totala åldern på bussen.")
            print("4. Beräkna den genomsnittliga åldern.")
            print("5. Skriv ut den passagerare med högst ålder.")
            print("6. Sortera bussen efter ålder.")
            print("7. Kolla passagerare med viss ålder.")
            print("8. Adda resterande passagerare automatiskt med random åldrar mellan 1, 90 år.")
            print("9. Avsluta.")


            val = input()
            #La till en match and case för valen i menyn. Lagt till att om bussen är tom så skriv ett meddelande ut också.
            match val:
                #Val för menyn 1 anropar funktionen add_passagerare, dä man lägger till passagerare
                 case "1":
                     if self.add_passagerare():
                         print("Passagerare tillagd.")
                #Val meny 2 som anropar funktionen skriv_ut_buss som skriver ut alla i bussen
                 case "2":
                      if self.skriv_ut_buss():
                          print("Alla passagerare i en lista.")
                      else:
                          print("Finns inga passagerare på bussen.")
                #Val meny 3 som anropar funktionen totala_alder som kollar totala ålder i bussen
                 case "3":
                      total_age = self.totala_alder()
                      if total_age:
                        print(f"Totala ålder på bussen: {total_age}")
                      else:
                        print("Det finns inga passagerare på bussen.")
                #Val av meny 4 anropar funktionen calc_average_age, räknar ut genomsnittliga ålder på bussen
                 case "4":
                    average_age = self.calc_average_age()
                    if average_age:
                        print("Medelålder på bussen:", average_age)
                    else:
                        print("Det finns inga passagerare på bussen.")
                #Val meny 5 anropar funktonen find_age, hittar de mellan åldrarna du skriver in
                 case "5":
                    oldest_age = self.find_age()
                    if oldest_age:
                        print("Den äldsta passageraren är", oldest_age, "år gammal")

                    else:
                        print("Det finns inga passagerare på bussen.")
                #Val 6 anropar funktioonen sort_buss_age, sorterar bussen lägsta till äldsta
                 case "6":
                    if self.passagerare:
                        self.sort_buss_age()  
                        print("Passagerarna är nu sorterade efter ålder.")
                    else:
                        print("Bussen är tom - ingen sortering möjlig.")
                #Val 7 anropar funktionen find_ages_by_range, hittar de som är emellan åldern du skrivit in
                 case "7":
                    ages = self.find_ages_by_range()
                    if ages:
                        print("Passagerare i det valda åldersintervallet:")
                        for age in ages:
                            print(age)

                    else:
                        print("Hittade inga passagerare i det valda åldersintervallet.")
                #val 8 anropar funktionen adda_random_passagerare, som lägger till 25 random passagerare.
                 case "8":
                    self.adda_random_passagerare()
                #val 9 anropar funktionen som avlsutar simulationen.
                 case "9":
                      avsluta_simulering()
                 case _:
                      print(f"Felaktigt val: '{val}'.")



    # Lägg till passagerare. skriv in ålder på passagerare då jag inte lägger till kön, om bussen är full så kan ingen stiga på. 
    #Och ett meddelande skrivs ut att det är fullt.
    def add_passagerare(self):
        try:
            alder = int(input("Ange ålder: "))
            #Skriver ut fel meddelande om användare inte skriver ett heltal.
        except ValueError:
            print("Felaktig ålder. Ange ett heltal.")
            return
        #Lägger till passagerare till 25st annars skriver ut bussen är full.
        if self.antal_passagerare < 25:
            self.passagerare.append(alder)
            self.antal_passagerare += 1
            print("Passagerare tillagd")

        else:
            print("Bussen är tyvärr full.")
        
    #Funktion för att skriva ut alla i bussen//skriv ut alla värden ifrån listan.
    def skriv_ut_buss(self):
        #Om listan är tom.
        if not self.passagerare:
            return False
        
        for passagerare in self.passagerare:
            print(passagerare)
        # Retunerar True om listan inte är tom.
        return True
        #Funktion för att skriva ut totala åldern på bussen. Funktionen beräknar åldern på alla och skickar tillbaka det till användaren.
    def totala_alder(self):

        if not self.passagerare:
            return 0

        total_age = 0
        for passagerare_age in self.passagerare:
            total_age += passagerare_age
        
        return total_age
    
    #Funktion för att räkna ut den genomsnittliga åldern på bussen, finns inga på bussen så skrivs ett meddelande ut att det inte finns några.
    def calc_average_age(self):

        if not self.passagerare:
            return None
        #Använder existerande funktion
        total_age = self.totala_alder()
        average_age = total_age / self.antal_passagerare

        return average_age

    #Funktion för att få fram den äldsta i bussen
    def find_age(self):

        if not self.passagerare:
            return None
        #Använder funktionen max som tar fram max i listan passagerare, man kan också använda funktionen max som finns i python
        #Men jag gjorde en algortim som itererar genom alla passagerare istället annars hade man kunnat använda koden nedan.
       # return max(self.passagerare)
        oldest_age = self.passagerare[0]  
        for passenger_age in self.passagerare[1:]:  # Iterera för att jämföra
            if passenger_age > oldest_age:
                oldest_age = passenger_age
        return oldest_age

    #Funktion för att sortera bussen, använvder mig av en inbyggd funktion i python
    def sort_buss_age(self):

        self.passagerare.sort()
    
    #Funktion för att kolla viss åldersspan i bussen exempel mellan 45-55 år, om det finns några passagerare där emellan.
    
    def find_ages_by_range(self):
        #Fråga användaren vilka åldrar den vill kolla

        try:
            min_age = int(input("Ange lägsta ålder: "))
            max_age = int(input("Ange högsta ålder: "))

            passagerare_in_range = []
            for passagerare_age in self.passagerare:
                if min_age <= passagerare_age <= max_age:
                    passagerare_in_range.append(passagerare_age)

            return passagerare_in_range
        
        except ValueError:
            print("Felaktigt åldersinmatning. Försök igen.")
            return None

    
    
    
    #Funktion för att adda random passagerare automatiskt, för att slippa läggsa till alla 1 och 1, detta lägger till resterande
    #av passsagerare om du har exempel lagt till 5 st redan. Lägger till 25st till bussen.
    def adda_random_passagerare(self):

        num_passagerare_to_add = min(25, 50 - self.antal_passagerare) #Automatiskt så att de inte lägger till fler än 25.

        for _ in range(num_passagerare_to_add):
            random_age = random.randint(1, 90) #Lägger random ålder mellan 1, 90 år
            self.passagerare.append(random_age)
            self.antal_passagerare += 1

        print(f"{num_passagerare_to_add} passagerare har lagts till.")

    

        

 #Funktion för att avlsuta simulatorn. Denna funktionen ligger utanför klassen buss för att få den att fungera.
def avsluta_simulering():
    print("Simulering avslutas...")
    exit()
