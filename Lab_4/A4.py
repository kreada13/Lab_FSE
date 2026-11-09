import re
def IsValidNumber(cardNumber):
    return cardNumber.isdigit() and len(cardNumber) in [13, 15, 16]
def getCheckSum(cardNumber):
    checkSum = 0
    digits = cardNumber[::-1]
    for i in range(len(digits)):
        digit = int(digits[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        checkSum = checkSum + digit
    return checkSum
def isValidCheckSum(checkSum):
    return checkSum % 10 == 0
def getCardType(cardNumber):
    if len(cardNumber) == 13 or len(cardNumber) == 16 and cardNumber.startswith("4"):
        return "Visa"
    if len(cardNumber) == 15 and cardNumber.startswith("34") or cardNumber.startswith("37"):
        return "American Express"
    if len(cardNumber) == 16 and re.match(r'5[1-5]', cardNumber[:2]):
        return "Master Card"
    return "Invalid"
cardNumber = input("Enter Card Number: ")
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        print(getCardType(cardNumber))
    else:
        print("Invalid checksum")
else:
    print("Wrong Input. Try again...")