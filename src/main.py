import datetime
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