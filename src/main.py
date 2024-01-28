import datetime

INVOICES = []

def validate_date(date):
    if date == "today":
        return
    else:
        try: 
            datetime.date.fromisoformat(date)
        except ValueError:
            raise ValueError("Incorrect data format, expected: YYYY-MM-DD")
        
def enter_date():
    sample_date = input("Enter the invoice date (YYYY-MM-DD):")
    validate_date(sample_date)
    return sample_date

def enter_amount():
    try:
        amount = float(input("Enter invoice cost: "))
    except ValueError:
        raise ValueError("Inocorrect data type, expected float")
    return amount
    
def enter_currency():
    currency = input("Enter currency name: ")
    return currency
    
def get_user_data():
    date = enter_date()
    amount = enter_amount()
    currency = enter_currency()
    temp = []
    temp.append(date)
    temp.append(amount)
    temp.append(currency)
    INVOICES.append(temp)
    print(INVOICES)

get_user_data()