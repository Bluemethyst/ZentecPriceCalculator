from colorama import Fore, init

init(autoreset=True)

# Decoration, ignore this
print(
    Fore.BLUE
    + """\
  ______          _              _____      _             _____      _            _       _             
 |___  /         | |            |  __ \    (_)           / ____|    | |          | |     | |            
    / / ___ _ __ | |_ ___  ___  | |__) | __ _  ___ ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / / / _ \ '_ \| __/ _ \/ __| |  ___/ '__| |/ __/ _ \ | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  / /_|  __/ | | | ||  __/ (__  | |   | |  | | (_|  __/ | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 /_____\___|_| |_|\__\___|\___| |_|   |_|  |_|\___\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                                        
                                                                                                        """
    + Fore.RESET
)

print(Fore.LIGHTBLUE_EX + "Created by Caleb" + Fore.RESET)
print(Fore.RED + "Press 'q' or 'Ctrl + C' anytime to exit." + Fore.RESET)

# Declare variables
i = 0

# Loop the program until q or Ctrl + C is pressed
while i <= 10:
    inputStr = input(Fore.CYAN + "Input Value... " + Fore.YELLOW + Fore.RESET).lower()
    # Check to see if the input is a Q for exiting
    if inputStr == "q":
        exit()
    if inputStr == "hello":
        print(Fore.YELLOW + "Hey adrian :D" + Fore.RESET)
        continue
    # Check to see if the input is a number
    try:
        inputInt = float(inputStr)
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid number." + Fore.RESET)
        continue

    # Check to see what multiple the input needs to be multiplied by
    if inputInt < 10:
        # Print the rounded number
        print(round(inputInt * 2, 2))

    if 9.99 < inputInt < 15:
        print(round(inputInt * 1.9, 2))

    if 14.99 < inputInt < 20:
        print(round(inputInt * 1.8, 2))

    if 19.99 < inputInt < 25:
        print(round(inputInt * 1.75, 2))

    if 24.99 < inputInt < 30:
        print(round(inputInt * 1.7, 2))

    if 29.99 < inputInt < 35:
        print(round(inputInt * 1.65, 2))

    if 34.99 < inputInt < 40:
        print(round(inputInt * 1.6, 2))

    if 39.99 < inputInt < 45:
        print(round(inputInt * 1.55, 2))

    if 44.99 < inputInt < 60:
        print(round(inputInt * 1.5, 2))

    if 59.99 < inputInt < 70:
        print(round(inputInt * 1.48, 2))

    if 69.99 < inputInt < 80:
        print(round(inputInt * 1.47, 2))

    if 79.99 < inputInt < 90:
        print(round(inputInt * 1.46, 2))

    if 89.99 < inputInt < 100:
        print(round(inputInt * 1.45, 2))

    if 99.99 < inputInt < 110:
        print(round(inputInt * 1.44, 2))

    if 109.99 < inputInt < 120:
        print(round(inputInt * 1.43, 2))

    if 119.99 < inputInt < 130:
        print(round(inputInt * 1.42, 2))

    if 129.99 < inputInt < 140:
        print(round(inputInt * 1.41, 2))

    if 139.99 < inputInt < 150:
        print(round(inputInt * 1.4, 2))

    if 149.99 < inputInt < 160:
        print(round(inputInt * 1.39, 2))

    if 159.99 < inputInt < 170:
        print(round(inputInt * 1.38, 2))

    if 169.99 < inputInt < 180:
        print(round(inputInt * 1.37, 2))

    if 179.99 < inputInt < 190:
        print(round(inputInt * 1.36, 2))

    if 189.99 < inputInt < 200:
        print(round(inputInt * 1.35, 2))

    if 199.99 < inputInt < 225:
        print(round(inputInt * 1.345, 2))

    if 224.99 < inputInt < 250:
        print(round(inputInt * 1.34, 2))

    if 249.99 < inputInt < 300:
        print(round(inputInt * 1.335, 2))

    if 299.99 < inputInt < 375:
        print(round(inputInt * 1.33, 2))

    if 374.99 < inputInt < 475:
        print(round(inputInt * 1.325, 2))

    if 474.99 < inputInt < 550:
        print(round(inputInt * 1.32, 2))

    if 549.99 < inputInt < 650:
        print(round(inputInt * 1.315, 2))

    if 649.99 < inputInt < 750:
        print(round(inputInt * 1.31, 2))

    if 749.99 < inputInt < 850:
        print(round(inputInt * 1.305, 2))

    if 849.99 < inputInt < 1000:
        print(round(inputInt * 1.3, 2))

    if 999.99 < inputInt < 1100:
        print(round(inputInt * 1.295, 2))

    if 1099.99 < inputInt < 1200:
        print(round(inputInt * 1.29, 2))

    if 1199.99 < inputInt < 1300:
        print(round(inputInt * 1.285, 2))

    if 1299.99 < inputInt < 1400:
        print(round(inputInt * 1.28, 2))

    if 1399.99 < inputInt < 1500:
        print(round(inputInt * 1.275, 2))

    if 1499.99 < inputInt < 1600:
        print(round(inputInt * 1.27, 2))

    if 1599.99 < inputInt < 1700:
        print(round(inputInt * 1.265, 2))

    if 1699.99 < inputInt < 1800:
        print(round(inputInt * 1.26, 2))

    if 1799.99 < inputInt < 1900:
        print(round(inputInt * 1.225, 2))

    if 1899.99 < inputInt < 2000:
        print(round(inputInt * 1.25, 2))

    if inputInt > 1999.99:
        print(round(inputInt * 1.2, 2))

    if inputInt == 0:
        print(
            Fore.RED
            + "An expected error occured, stop trying to multiply by zero man you already know the answer"
            + Fore.RESET
        )
