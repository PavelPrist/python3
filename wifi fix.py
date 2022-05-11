print('Reboot the computer and try to connect.\n   Enter yes for yes or no for no." \nDo you fix problem?')

respond = str(input('Write yes or no -- '))

if respond != 'yes' and respond != 'no':
    print("Enter 'yes' for yes or 'no' for no.")
    respond = str(input('Write yes or no -- '))
else:
    print()

if respond == 'yes':
    print('Congratulation!')
# elif respond == 'no':
else:
    print('Restart router and try reconnect. \nDo you fix problem?')
    respond1 = str(input('Write yes or no-- '))
    if respond1 == 'yes':
        print('Congratulation!')
    # elif respond1 == 'no':
    else:
        print('Check wire. \nDo you fix problem?')
        respond2 = str(input('Write yes or no-- '))
        if respond2 == 'yes':
            print('Congratulation!')
        # elif respond2 == 'no':
        else:
            print('Replace router close to computer. \nDo you fix problem?')
            respond3 = str(input('Write yes or no-- '))
            if respond3 == 'yes':
                print('Congratulation!')
            # elif respond3 == 'no':
            else:
                print(" ʕʘ‿ಠ ¯\_(ツ)_/¯     Buy new router. Or throw out your computer!!!")
