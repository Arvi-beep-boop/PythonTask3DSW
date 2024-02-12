import datetime
import API
INVOICES = []
        
def enter_date():
    sample_date = input("Enter the invoice date (YYYY-MM-DD):")
    API.validate_date(sample_date)
    return sample_date

def enter_amount():
    while True:
        try:
            amount = float(input("Enter invoice cost: "))
            if amount < 0:
                print("The amount cannot be negative ")
        except ValueError:
            raise ValueError("Inocorrect data type, expected float")
        return amount
    
def enter_currency():
    currency = input("Enter currency name: ")
    # TO DO: handle incorrect currency name
    return currency

# Płatność użytkownika? 
def get_user_data():
    # date = enter_date()
    # amount = enter_amount()
    # currency = enter_currency()
    temp = [enter_date(), enter_amount(), enter_currency()]
    # temp.append(date)
    # temp.append(amount)
    # temp.append(currency)
    INVOICES.append(temp)
    print(INVOICES)

get_user_data()

            
def enter_currency():
    return input("Enter currency code ")
            
 
def main():
     amount= enter_amount()
     currency= enter_currency()
     date= enter_date()
     print(f"Invoice amount: {amount} {currency}")
     print(f"Date of invoice: {date}")
     
if __name__=="__main__":
     main()

