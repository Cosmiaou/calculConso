import decimal

fuel = 0
distance = 0
command = ''


def change_data(text):
    while True:
        value = input(text)

        try:
            value = float(value)
            break
        except:
            print("Please enter a number and use a period to indicate the decimal place.")

    return value


while command != 'end':
    print('\nPlease input a command, or simply indicate the fuel consumption in liter/gallons per kilometer/miles (ex. 7.2)\n')
    command = input()

    if command == 'end':
        quit(0)
    elif command == 'help':
        print("\n HELP :\n"
              "- ‘change_distance’: allows you to change the recorded distance;\n"
              "- ‘change_fuel’: allows you to change the fuel price;\n"
              "- ‘print_distance’: allows you to display the fuel price;\n"
              "- ‘print_fuel’: displays the fuel price;\n"
              "- ‘help’: displays the list of commands\n"
              "- ‘end’: exits the program\n")
        continue
    elif command == 'change_distance':
        distance = change_data('\nPlease input the monthly distance : ')
        continue
    elif command == 'change_fuel':
        fuel = change_data('\nPlease input the price of fuel : ')
        continue
    elif command == 'print_distance':
        print(decimal.Decimal(distance).quantize(decimal.Decimal('0.1')))
        continue
    elif command == 'print_fuel':
        print(decimal.Decimal(fuel).quantize(decimal.Decimal('0.001')))
        continue

    try:
        consumption = float(command)
    except:
        print("This is not a valid command. If you want to perform a calculation, please enter a number and use a period to specify the decimal place.")

    else:

        consumption /= 100
        consumption *= fuel
        monthlyPrice = consumption * distance

        resultConsumption = decimal.Decimal(consumption).quantize(decimal.Decimal('0.01'))
        resultPrice = decimal.Decimal(monthlyPrice).quantize(decimal.Decimal('0.01'))

        print('\nThe price per km/miles is ', resultConsumption, ', and the mensual price is ', resultPrice)
