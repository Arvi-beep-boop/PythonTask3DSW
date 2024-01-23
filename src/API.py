import requests

# TO DO: 
# handle errors
# handle different date formats
# handle no-data on specified date (get the closest data to required one)

# Returns default A table at specified date' 
def get_NBP_table(date):
    body = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{date}')
    return body.json()
    
# Returns currency average rate at specified date, accepts "today" 
def get_Currency_avg(code, date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json'
    response = requests.get(url)
    json = response.json()
    print(json)
    
# Playground
m_currency_code = input("Currency code: ")
m_date = input("Date (YYYY-MM-DD): ")
get_Currency_avg(m_currency_code, m_date)