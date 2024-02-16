import API
import csv
import datetime

m_fields = [
    'INVOICE DATE','INVOICE VALUE','INVOICE CURRENCY','INVOICE VALUE PLN',
    'PAYMENT DATE','PAYMENT VALUE','PAYMENT CURRENCY', 'PAYMENT VALUE PLN'
    ]
m_file = 'INVOICES.csv'
m_currencies = ['USD', 'GBP', 'EUR', 'PLN']

# Gets date from user and validates it
def enter_date():
    while True:
        date = input("Enter the date (YYYY-MM-DD):")
        if(API.validate_date(date) == False):
            continue
        else:
            return date

# Gets value e.g 20.60
def enter_amount():
    while True:
        try:
            amount = float(input("Enter value: "))
            if amount < 0:
                print("The amount cannot be negative ")
                continue
        except ValueError:
            print("Inocorrect data type, expected float (e.g. 20.50): ")
            continue
        return str(amount)

# Gets currency name e.g USD 
def enter_currency():
    while True:
        currency = input("Enter currency name: ").upper()
        if currency in m_currencies:
            return currency
        else:
            print(f'Currency {currency} is invalid try: USD, GBP, PLN or EUR')

# Shows all invoices (raw data from .csv file)
def show_all_invoices():
    file = open(m_file, 'r')
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        print(str(i)+'.', row)
    file.close()
    input("Press key to continue") 

# Shows payments statuses for each invoice(line) number
def show_payment_status():
    file = open(m_file, 'r')
    reader = csv.DictReader(file)
    status = ''
    val = 0
    for i, row in enumerate(reader):
        if i == 0: continue
        try:
            if row['PAYMENT VALUE PLN']:
                val = float(row['INVOICE VALUE PLN']) - float(row['PAYMENT VALUE PLN'])
                if val > 0.001:
                    status = "UNDERPAID"
                elif val < 0:
                    status = "OVERPAID"
                    val = -val
                elif val < 0.001:
                    status = 'PAID'
        except ValueError or TypeError:
            status = "UNKNOWN"
            val = 'N'
        if str(val) != 'N': val = round(val, 2)
        print(f'Invoice No. {str(i)+'.'} issued {row['INVOICE DATE']} for {row['INVOICE VALUE']} {row['INVOICE CURRENCY']} is {status} by {val} PLN')
    file.close()
    input("Press key to continue") 

# Adds new invoice data (date, currency, value) to .csv file
def add_new_invoice():
    file = open(m_file, 'a', newline='')
    writer = csv.writer(file)
    date, currency, amount = enter_date(), enter_currency(), enter_amount()
    if currency == 'PLN':
        writer.writerow([date,amount,currency, amount])
    else:
        writer.writerow([date,amount,currency, API.calculate_to_pln(currency, date, float(amount))])
    file.close()
    input("Press key to continue") 

# Adds payment for selected invoice(line) number in .csv file, multiple payments for one invoice are available
def add_new_payment():
    read = open(m_file,'r')
    temp = [m_fields]
    reader = csv.DictReader(read)
    show_all_invoices()
    # while True:
    num = int(input("Enter line number:" ))
        # if num < len(reader): #object of type 'DictReader' has no len() TO DO: FIX
        #     break
        # else: print("Inavlid line number")
    currency, date, amount = enter_currency(), enter_date(), enter_amount()

    # CHECK DATA INTEGRITY
    for row in enumerate(reader, start=1):
        if i > 0:
            if i == num:
                if(row['PAYMENT DATE'] and row['PAYMENT CURRENCY']):
                    if(currency != row['PAYMENT CURRENCY']):
                        print(f"Making multiple payments in different currencies is not allowed, expected {row['PAYMENT CURRENCY']}")
                        return
                if(datetime.date.fromisoformat(date) < datetime.date.fromisoformat(row['INVOICE DATE'])):
                    print(f'Invalid date, paying for invoice earlier than invoice date is invalid')
                    return
    # ADD PAYMENT
    for i, row in enumerate(reader, start=1):
        if i > 0:
            if i == num:
                payment_val = 0 if not row['PAYMENT VALUE'] else float(row['PAYMENT VALUE'])
                payment_val_pln = 0 if not row['PAYMENT VALUE PLN'] else float(row['PAYMENT VALUE PLN'])
                if currency == "PLN":
                    payed = payment_val + amount
                else:
                    payed = payment_val_pln + (API.calculate_to_pln(currency,date, amount))

                temp.append([
                    row['INVOICE DATE'], row['INVOICE VALUE'], row['INVOICE CURRENCY'], row['INVOICE VALUE PLN'],
                    date, str(float(amount) + payment_val), currency, payed])
            else:
                row_values = []
                for field in m_fields:
                    row_values.append(row[field])
                temp.append(row_values)
    read.close()
    write = open(m_file, 'w', newline='')
    writer = csv.writer(write)
    writer.writerows(temp)
    write.close()
    input("Press key to continue") 

# Returns exchange rate for specified currency and date
def get_exchange_rate():
    currency = enter_currency()
    if currency == 'PLN':
        value = 1
    else: 
        value = API.get_Currency_avg(currency, enter_date())
    print(f'Current exchange rate for {currency} is: {value} PLN')
    input("Press key to continue") 

m_userMenu = {
    1: ["Add New Invoice", add_new_invoice], 
    2: ["View All Invoices", show_all_invoices],
    3: ["Add New Payment", add_new_payment],
    4: ["Get Exchange Rate", get_exchange_rate],
    5: ["View Payment Status", show_payment_status], 
    6: ["Quit application", quit]
}

# MAIN LOOP
while True:
    for option in m_userMenu: 
        print(str(option) + ".", m_userMenu[option][0])
    try:    
        selection = int(input("Select option: "))
    except ValueError: input('Option number needed, press key to try again'); continue
    m_userMenu[selection][1]()
