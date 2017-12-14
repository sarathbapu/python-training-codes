# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:01:37 2017
currency Converter from Google
@author: Sarath
"""
import sys

try :
	import requests
	from lxml import html
except :
	print("Install modules 'requests' and 'lxml' to continue")
	sys.exit()

'''
The below url is used to convert 10.24 USD to INR

URL : http://finance.google.com/finance/converter?a=10.24&from=USD&to=INR
Reponse type from URL is html page. 

'''

print('Welcome to Currency Converter.. !')
print('Press Ctrl+C to exit at any point of time')

try :
	print('\n\n\n\n\n')
    baseurl = 'http://finance.google.com/finance/converter'    
    initContext = requests.get(baseurl)
    initR = str(initContext.content)
    while True:
        try :
            amount = float(input('Enter the amount to convert :'))
        except ValueError :
            print( "Numerical values Only")
            continue
        
        try :
            currency1 = input('Enter Currency 1 :')
            searchString = 'value="'+currency1.upper()+'"'
            if not (searchString in initR ):
                raise ValueError
        except ValueError:
            print('Currency1 not available. Enter valid Currency ')
            continue
        
        try :
            currency2 = input('Enter Currency 2 :')
            searchString = 'value="'+currency2.upper()+'"'
            if searchString not in initR :
                raise ValueError
        except ValueError:
            print('Currency2 not available. Enter valid Currency ')
            
        inputParams = {'a':amount, 'from':currency1, 'to':currency2}

        resp = requests.get(baseurl, params=inputParams)
        
        respContent = str(resp.content)

        # Using the xpath to find the result
		# //*[@id="currency_converter_result"]/span

        respTree = html.fromstring(respContent)
        
        print(respTree.xpath(r'//*[@id="currency_converter_result"]/span')[0].text)
    
except KeyboardInterrupt :
    print("Thank you for using converter")
