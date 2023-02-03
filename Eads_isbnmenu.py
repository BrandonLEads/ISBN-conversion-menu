# main function
def main():
    # testing the menu
    choice = Menu()
    while (choice != 5):
        if (choice == 1):
            print ("Verify the check digit of an ISBN-10")
            VerifyISBN10()
        elif (choice == 2):
            print ("Verify the check digit of an ISBN-13")
            VerifyISBN13()
        elif (choice == 3):
            print ("Convert an ISBN-10 to a ISBN-13")
            convertISBN10_13()
        elif (choice == 4):
            print ("Convert an ISBN-13 to a ISBN-10")
            convertISBN13_10()
        elif (choice == 5):
            print("Have a nice day")

        print()
        print()
        choice = Menu()

# defining menu funtion
def Menu():
    # printing the menu   
    print("1. Verify the check digit of an ISBN-10")
    print("2. Verify the check digit of an ISBN-13")
    print("3. Convert an ISBN-10 to a ISBN-13")
    print("4. Convert an ISBN-13 to a ISBN-10")
    print("5. Exit")
    choice = int (input("Enter option: "))
    while (choice < 1 and choice > 5):
        choice = int (input("Enter option: "))
    return choice

# defining function to calculate check digit of isbn10
def calculateCheckDigitOfISBN10(isbn1):
    #loop through the digits in isbn
    multiplier = 1
    total=0
    for digit in isbn1:
        #leave last digit as it is check digit
        if multiplier < 10:
            # calculating the total
            total = total + (multiplier * int(digit))
        multiplier = multiplier + 1
    check=total%11
    return check

# defining function to calculate check digit of isbn13
def calculateCheckDigitOfISBN13(isbn1):
    #loop through the digits in isbn
    count = 0
    multiplier =  1
    total=0
    for digit in isbn1:
        #leave last digit as it is check digit
        if count < 12:
            if count % 2 == 0:
                multiplier = 1
            else:
                multiplier = 3
            # calculating the total
            total = total + (multiplier * int(digit))
        count = count + 1
    check= total%10
    return check


# defining function to Verify the check digit of an ISBN-10
def VerifyISBN10():
    isbn = input ("Enter ISBN-10 (#-##-######-#): ")
    #remove - from user input#
    isbn1 = isbn.replace('-', '')
    #get check digit
    check=calculateCheckDigitOfISBN10(isbn1)
    if (check == int(isbn1[9])):
        print(isbn + " is a valid isbn number")
    else:
        print("Invalid ISBN number. check digit should be " + str(check))


 
# defining function to Verify the check digit of an ISBN-13
def VerifyISBN13():
    isbn = input ("Enter ISBN-13 (###-#-##-######-#): ")
    #remove - from user input#
    isbn1 = isbn.replace('-', '')
    #get check digit
    check=calculateCheckDigitOfISBN13(isbn1)
    if (check == int(isbn1[12])):
        print(isbn + " is a valid isbn number")
    else:
        print("Invalid ISBN number. check digit should be " + str(check))

# defining function to convert 10 digit isbn to 13 digit
def convertISBN10_13():
    isbn = input ("Enter ISBN-10 (#-##-######-#): ")
    #prefix 978-
    isbn13 = "978-" + isbn
    #remove - to calculate check digit
    isbn1 = isbn13.replace('-', '')
    #get check digit
    check=calculateCheckDigitOfISBN13(isbn1)
    #concatenate check digit
    isbn13 = isbn13[0:len(isbn13)-1] + str(check)
    print("ISBN13 will be = " + isbn13)

# defining function to convert 13 digit isbn to 10 digit
def convertISBN13_10():
    #getting user input
    isbn = input ("Enter ISBN-13 (###-#-##-######-#): ")
    #removing first 4 characters
    isbn10 = isbn[4:]
    #remove - # 
    isbn1 = isbn10.replace('-', '')
    #get check digit
    check = calculateCheckDigitOfISBN10(isbn1)
    #concatenate check digit
    isbn10 = isbn10[0:len(isbn10)-1] + str(check)
    print("ISBN10 will be = " + isbn10)
    
main()
