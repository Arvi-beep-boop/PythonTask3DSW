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

# def enter_amount():
    
# def enter_currency():
    
# def get__data():
    # date = get_date
    # curr = get_currency
    # amount = get_invoice
    # temp = []
    # temp.append(get_date())
    # ....
    # INVOICES.append(temp)


    
enter_date()

#dodanie do tablicy 3 zmiennych (kwota, data, waluta)
# 