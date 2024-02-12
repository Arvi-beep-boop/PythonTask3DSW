import requests
import datetime

# TO DO: Move date format validation to another script, do checking if there's data from nbp for specified date here instead
# Datetime format validation: 
def validate_date(date):
    if date == "today":
        return
    else:
        try: 
            datetime.date.fromisoformat(date)
        except ValueError:
            raise ValueError("Incorrect data format, expected: YYYY-MM-DD")

# Currency code validation
# TO DO: think of adding a predefined file with all currency codes, what if data for -
# specified currency code is unavailable for that date? (at get_Currency_av()) 
def validate_currency_code(json, code):
    for rates in json[0]['rates']:
        if rates['code'] == code:
            return
    raise ValueError(f"Incorrect currency code: {code}")
    
# TO DO: 
# handle errors
# handle different date formats (?) -> check for YYYY-MM-DD instead
# handle no-data on specified date (get the closest data to required one)

# Returns default A table at specified date' 
def get_NBP_table(date):
    body = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{date}')
    return body.json()
    
# Returns currency average rate at specified date, accepts "today" 
def get_Currency_avg(code, date):
    validate_date(date)
    validate_currency_code(get_NBP_table(date), code)
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json'
    response = requests.get(url)
    json = response.json()
    print(json['rates'][0]['mid'])
    # return json
    
# Playground
m_currency_code = input("Currency code: ")
m_date = input("Date (YYYY-MM-DD): ")
get_Currency_avg(m_currency_code, m_date)