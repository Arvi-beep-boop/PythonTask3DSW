import API
import csv

m_fields = [
    'INVOICE DATE','INVOICE VALUE','INVOICE CURRENCY','INVOICE VALUE PLN',
    'PAYMENT DATE','PAYMENT VALUE','PAYMENT CURRENCY', 'PAYMENT VALUE PLN'
    ]
m_file = 'INVOICES.csv'


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
            amount = float(input("Enter invoice cost: "))
            if amount < 0:
                print("The amount cannot be negative ")
        except ValueError:
            print("Inocorrect data type, expected float (e.g. 20.50): ")
            continue
           
        return str(amount)
    
def enter_currency():
    currency = input("Enter currency name: ").upper()
    # TO DO: handle incorrect currency name
    return currency

def show_all_invoices():
    file = open(m_file, 'r')
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        print(str(i)+'.', row)
    print("=" * 100)
    file.close()


def add_new_invoice():
    file = open(m_file, 'a', newline='')
    writer = csv.writer(file)
    date, currency, amount = enter_date(), enter_currency(), enter_amount()
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
                temp.append([
                    row['INVOICE DATE'], row['INVOICE VALUE'], row['INVOICE CURRENCY'], row['INVOICE VALUE PLN'],
                    date, amount, currency, API.calculate_to_pln(currency,date, amount)])
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
    API.get_Currency_avg(enter_currency(), enter_date())

m_userMenu = {
    1: ["Add new invoice", add_new_invoice], 
    2: ["View all invoices", show_all_invoices],
    3: ["Add new payment", add_new_payment],
    4: ["Get Exchange rate", get_exchange_rate],
    5: ["Quit application", quit]

}


    
# API.get_NBP_table('2024-02-11')

# MAIN LOOP
while True:
    # print main menu
    for option in m_userMenu: 
        print(str(option) + ".", m_userMenu[option][0])
# get option from user
    selection = int(input("Select option: "))
    m_userMenu[selection][1]()
