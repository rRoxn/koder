#Skriv in Fahrenheit

def fahrenheit_till_celcius(fahrenheit):
    """Denna funktionen kommer göra om inputen ifrån användare som är Fahrenheit till Celcius
        """
    celcius = (fahrenheit - 32) * 5 / 9
    return int(celcius)

#Få fahrenheit från användare
fahrenheit_input = int(input("Enter temperature in Fahrenheit: "))

#Konventera inputen till celcius
celcius = fahrenheit_till_celcius(fahrenheit_input)

#Printa ut graderna i celcius
print(fahrenheit_input, "Fahrenheit is equal to", celcius, "Celcius")