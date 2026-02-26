import requests
import json
def search_company(company_name):
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={company_name}"
    # ADD THIS LINE: It tells Yahoo you are a real browser
    headers = {'User-Agent': 'Mozilla/5.0'}
    # send the request to yahoo finance search API
    response = requests.get(url, headers=headers) # response is variable name , requests.get(url)--> it is telling that go yo url and get the data
    if response.status_code == 200: # if the response is successful (status code 200), then we can proceed to parse the data
        data = response.json() #The requests library knows that almost everyone getting data from the web wants it as a dictionary. So, it built the translation tool directly into the response object.When you write data = response.json(), the requests library does the json.loads() work for you behind the scenes. It's cleaner and faster to write.

        try: #if user writes anything that doesnt matches then because of "try" the whole code will not crash. This is error handling.
            ticker = data['quotes'][0]['symbol'] # we are accessing the first result in the quotes list and getting the symbol (ticker) of the company. quote is the latest information about the stock.
            return ticker # gives answer back to the main program
        except (IndexError, KeyError): # if there is an error in accessing the data (like if the company name is not found), we will catch that error and return None.
            return "No Ticker found for the company name provided. Please try with valid name."
    else:
        return "Connection Error."
        
# Testing Code
name = input("Enter the company name: ")
ticker_result = search_company(name)
print(f"Result for {name}: {ticker_result}")

        
