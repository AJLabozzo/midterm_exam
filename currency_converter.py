import re
import urllib.request
import json
import pprint as pp
import time
import sys

api_endpoint = "https://api.exchangerate-api.com/v4/latest/USD"

def page_exists(page):
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False

def input_valid(userInput):
    regexp = re.compile(r'^[A-Z]{3}$')
    if not regexp.search(userInput):
        return False
    else:
        return True
    

def convert_currency(amount,from_code,to_code):
    
    if page_exists(api_endpoint):
            page = urllib.request.urlopen(api_endpoint)
            content = page.read().decode("utf-8")
            data = json.loads(content)
            if not data:
                return "no data"
            rates = data["rates"]
            if not rates:
                return "no rates"
            if from_code not in rates:
                return "FROM currency code not found"
            if to_code not in rates:
                return "TO currency code not found"
            from_rate = float(rates[to_code])
            to_rate = float(rates[to_code])
            
    else:
        return "ERROR:invalid API endpoint"
        
    if from_rate == to_rate:
        result = amount
    elif from_rate < to_rate:
        result = amount * (from_rate/to_rate)
    else:
        result = amount * to_rate
    
    return "{} in {} = {} in {}".format(amount,from_code,result,to_code)
    
        
    
def main():
    
    while(True):
        user_input = input("Enter amount to be converted(q to quit):")
        if(user_input == 'q' or user_input == 'Q'):
            print("Exiting")
            break
        else:
            try:
                amount = int(user_input)
            except ValueError:
                try:
                    amount = float(user_input)
                except:
                    print("Invalid amount {}".format(user_input))
                    continue
        
        user_input2 = input("Enter FROM currency 3 letter code:")
        if not input_valid(user_input2):
            print("Invalid currency code {}".format(user_input2))
            continue
            
        user_input3 = input("Enter TO currency 3 letter code:")
        if not input_valid(user_input3):
            print("Invalid currency code {}".format(user_input3))
            continue
        
        print(convert_currency(amount,user_input2,user_input3))
        
if __name__ == '__main__':
    main()