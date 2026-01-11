def menu(): 
    print('\nUnit Conversion Calculator Menu:') 
    print('1. Kilometer to Meter') 
    print('2. Meter to Kilometer') 
    print('3. Meter to Centimeter') 
    print('4. Centimeter to Millimeter') 
    print('5. Quit') 
    choice = int(input("Enter your choice (1-5): ")) 
    return choice 
 
def kilometer_to_meter(): 
    num = float(input("Enter First Number: ")) 
    result = num * 1000 
    print(result, "meters") 
 
def meter_to_kilometer(): 
    num = float(input("Enter First Number: ")) 
    result = num / 1000 
    print(result, "kilometers") 
 
def meter_to_centimeter(): 
    num = float(input("Enter First Number: ")) 
    result = num * 100 
    print(result, "centimeters") 
 
def centimeter_to_millimeter(): 
    num = float(input("Enter First Number: ")) 
    result = num * 10 
    print(result, "millimeters") 
 
def main(): 
    while True: 
        choice = menu() 
        if choice == 1: 
            kilometer_to_meter() 
        elif choice == 2: 
            meter_to_kilometer() 
        elif choice == 3: 
            meter_to_centimeter() 
        elif choice == 4: 
            centimeter_to_millimeter() 
        elif choice == 5: 
            print("Thank you for using the Conversion Calculator. Goodbye!") 
            break 
        else: 
            print("Invalid choice. Please select a number between 1 and 5.") 
 
if __name__ == "__main__": 
    main()
