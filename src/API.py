import requests
import datetime

# Datetime format validation, returns False if validation is unsuccesfull 
def validate_date(date):
    try: 
        if datetime.date.fromisoformat(date) < datetime.date(2002,1,2):
            print("Only dates later than 2002-01-02 are accepted")
            return False
        datetime.date.fromisoformat(date)
    except ValueError:
        print("Incorrect data format, expected: YYYY-MM-DD")
        return False

# Currency code validation
def validate_currency_code(json, code):
    for rates in json[0]['rates']:
        if rates['code'] == code:
            return
    raise ValueError(f"Incorrect currency code: {code}")
    
# Returns default A table at specified date, yields 0 if data is unavailable for a specific date
def get_NBP_table(date):
    response = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{date}')
    if response.status_code == 404:
        return 0
    else:
        return response.json()

# Returns currency average rate at specified date
def get_Currency_avg(code, date):
    m_date = date
    while True:
        if get_NBP_table(m_date) == False:
            m_date = str(datetime.date.fromisoformat(m_date) - datetime.timedelta(days=1))
        else:
            break
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{m_date}/?format=json'
    response = requests.get(url)
    json = response.json()
    return json['rates'][0]['mid']

# Returns value in PLN for specified currency, date and value
def calculate_to_pln(code, date, value):
    if code == "PLN": return
    return round(float(get_Currency_avg(code, date))*float(value), 2)