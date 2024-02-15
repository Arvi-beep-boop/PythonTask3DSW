import API
import csv
import datetime

m_fields = [
    'INVOICE DATE','INVOICE VALUE','INVOICE CURRENCY','INVOICE VALUE PLN',
    'PAYMENT DATE','PAYMENT VALUE','PAYMENT CURRENCY', 'PAYMENT VALUE PLN'
    ]
m_file = 'INVOICES.csv'
m_currencies = ['USD', 'GBP', 'EUR', 'PLN']

def enter_date():
    while True:
        date = input("Enter the invoice date (YYYY-MM-DD):")
        if(API.validate_date(date) == False):
            continue
        else:
            return date

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
    
def enter_currency():
    while True:
        currency = input("Enter currency name: ").upper()
        if currency in m_currencies:
            return currency
        else:
            print(f'Currency {currency} is invalid try: USD, GBP, PLN or EUR')

def show_all_invoices():
    file = open(m_file, 'r')
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        print(str(i)+'.', row)
    print("=" * 100)
    file.close()

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
        print(f'Invoice No. {str(i)+'.'} is {status} by {val} PLN')
    file.close()

def add_new_invoice():
    file = open(m_file, 'a', newline='')
    writer = csv.writer(file)
    date, currency, amount = enter_date(), enter_currency(), enter_amount()
    if currency == 'PLN':
        writer.writerow([date,amount,currency, amount])
    else:
        writer.writerow([date,amount,currency, API.calculate_to_pln(currency, date, float(amount))])
    file.close()

def add_new_payment():
    read = open(m_file,'r')
    temp = [m_fields]
    show_all_invoices()
    num = int(input("Enter line number:" ))
    reader = csv.DictReader(read)
    for i, row in enumerate(reader, start=1):
        if i > 0:
            if i == num:
                currency, date, amount = enter_currency(), enter_date(), enter_amount()

                # CHECK DATA INTEGRITY
                if(row['PAYMENT DATE'] and row['PAYMENT CURRENCY']):
                    if(currency != row['PAYMENT CURRENCY']):
                        print(f"Making multiple payments in different currencies is not allowed, expected {row['PAYMENT CURRENCY']}")
                        break
                if(datetime.date.fromisoformat(date) < datetime.date.fromisoformat(row['INVOICE DATE'])):
                    print(f'Invalid date, paying for invoice earlier than invoice date is invalid')
                    break
                
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

def get_exchange_rate():
    currency = enter_currency()
    if currency == 'PLN':
        value = 1
    else: 
        value = API.get_Currency_avg(currency, enter_date())
    print(f'Current exchange rate for {currency} is: {value} PLN')

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
    # print main menu
    for option in m_userMenu: 
        print(str(option) + ".", m_userMenu[option][0])
# get option from user
    selection = int(input("Select option: "))
    m_userMenu[selection][1]()