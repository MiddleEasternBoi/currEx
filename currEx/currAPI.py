import requests
import json
from ISOdict import *


def helpList():
    '''Prints a formatted list of ISO codes and their corresponding names from the ISOdict module'''

    # uses the ISOcodes module to get the list of ISO codes from an Excel document
    ISO_codes = ISOcodes()
    ISO_codes = ISO_codes[0]
    for i in ISO_codes:
        print(i, ":", ISO_codes[i])

def userparams():
    '''Functions similar to a main. Takes in user parameters continuously and runs the command, including any conversions specified.'''

    print("To convert: type: amount, 3-letter ISO code for currency to exchange from, 3-letter ISO code for currency to exchange to, digits to round to")
    print("\nex: 20 USD EUR 2")
    print("\nType 'help' for a list of ISO 3-letter currency codes.")
    print("\nType 'quit' to exit")

    while True:
        userInput = input('> ')
        tokens = userInput.split(' ')
        
        if "help" in tokens:
            helpList()
        elif "quit" in tokens:
            break
        else:
            # prints the converted amount without any rounding specified 
            if len(tokens) == 3:
                amount = tokens[0]
                fromamount = tokens[1]
                toamount = tokens[2]
                response = callAPI(toamount, fromamount, amount)
                printConverted(response, toamount, "none")
            
            # prints the converted amount with rounding specified
            elif len(tokens) == 4:
                amount = tokens[0]
                fromamount = tokens[1]
                toamount = tokens[2]
                digitsRounding = tokens[3]
                response = callAPI(toamount, fromamount, amount)
                printConverted(response, toamount, digitsRounding)
            else:
                # need either 3 or 4 args - continues to accept input
                print("incorrect number of arguments!")

def callAPI(toamount, fromamount, amount):
    '''Calls a get request from the Currency Data API according to the specified ISO to convert from (fromamount), the ISO to convert to (toamount), and the amount to convert (amount)'''

    url = f"https://api.apilayer.com/currency_data/convert?to={toamount}&from={fromamount}&amount={amount}"

    payload = {}

    # unique API key according to the Currency Data API "Free Plan"
    headers = {
        "apikey": "7LxmZVOkUTsuqmvuxY07S8NJDfWR8i1B"
    }

    response = requests.get(url, headers=headers, data=payload)

    return response

def printConverted(response, toamount, digitsRounding):
    '''Prints the converted amount. Converts the get request (response) to JSON and prints the resulting currency conversion with the specified ISO (toamount) and rounded to digitsRounding'''

    # json just creates a dictionary and can be accessed like normal
    try:
        converted = response.json()['result']
        if digitsRounding != "none":
            converted = round(converted, int(digitsRounding))
        print(converted, toamount.upper())
    
    # if get request failed and response is empty, likely because of misformatted user input
    except:
        print("invalid input! (check formatting, ISO code spelling)")
