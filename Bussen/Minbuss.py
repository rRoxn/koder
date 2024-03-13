"""Detta är andra klassen som skall anroppa den andra filen för att kunna köra programmet."""

from Bussenklass import Buss


class Program:
    def __init__(self, *args):
     
        minbuss = Buss()
        minbuss.run()

   
        input("Press Enter to continue . . . ")


if __name__ == "__main__":
    # skapa en instans (kopia) av klassen Program 
    my_program = Program()