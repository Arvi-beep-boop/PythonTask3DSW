import requests
import datetime

# Datetime format validation: 
def validate_date(date):
    if date == "today":
        return
    else:
        if datetime.date.fromisoformat(date) < datetime.date(2002,1,2):
                print("Only dates later than 2002-01-02 are accepted")
                return False
        try: 
            datetime.date.fromisoformat(date)
        except ValueError:
            print("Incorrect data format, expected: YYYY-MM-DD")
            return False

# Currency code validation
# TO DO: think of adding a predefined file with all currency codes, what if data for -
# specified currency code is unavailable for that date? (at get_Currency_av()) 
def validate_currency_code(json, code):
    for rates in json[0]['rates']:
        if rates['code'] == code:
            return
    raise ValueError(f"Incorrect currency code: {code}")
    
# Returns default A table at specified date
def get_NBP_table(date):
    response = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/A/{date}')
    if response.status_code == 404:
        return 0
    else:
        return response.json()

# Returns currency average rate at specified date, accepts "today" 
def get_Currency_avg(code, date):
    # validate_date(date)
    # validate_currency_code(get_NBP_table(date), code)
    m_date = date
    while True:
        if get_NBP_table(m_date) == False:
            m_date = str(datetime.date.fromisoformat(m_date) - datetime.timedelta(days=1))
            print(m_date)
        else:
            break
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{m_date}/?format=json'
    response = requests.get(url)
    json = response.json()
    return json['rates'][0]['mid']

def calculate_to_pln(code, date, value):
    if code == "PLN": return
    return round(float(get_Currency_avg(code, date))*value, 2)