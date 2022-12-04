import pandas
import os
import sys

sys.path.insert(0, './currEx')

def ISOcodes():
    '''Used to analyze an Excel spreadsheet of ISO codes and their corresponding names and converts them into a Python dictionary for the 'help' command'''
    print(os.getcwd())
    codes = pandas.read_excel('./currEx/CurrencyData.xlsx')
    codes_dict = codes.to_dict('records')
    return codes_dict