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

def enter_amount():
    while True:
        try:
            amount= float(input("Enter amount "))
            if amount < 0:
                print("The amount cannot be negative ")
            else:
                return amount
        except ValueError:
                print("Invalid amount format.Enter a number ")
                

            
def enter_currency():
    return input("Enter currency code ")


def enter_date():
    while True:
        try:
            data_str=input("Enter the invoice date  (RRRR-MM-DD):")
            data=datetime.datetime.strptime(data_str,'%Y-%m-%d')
            return data.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid format ")
            
 
def main():
     amount= enter_amount()
     currency= enter_currency()
     date= enter_date()
     print(f"Invoice amount: {amount} {currency}")
     print(f"Date of invoice: {date}")
     
if __name__=="__main__":
     main()

