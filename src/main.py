import API
import csv
# Maybe work only on csv file instead of arrays?
INVOICES = []
m_fields = ['INVOICE DATE','INVOICE VALUE','INVOICE CURRENCY','PAYMENT DATE','PAYMENT VALUE','PAYMENT CURRENCY']
m_file = 'INVOICES.csv'
# m_file = open("INVOICES.csv", 'a')
# m_writer = csv.writer(m_file)
# m_reader = csv.reader(m_file)

def enter_date():
    date = input("Enter the invoice date (YYYY-MM-DD):")
    API.validate_date(date)
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
    file.close()

# Invoice data
# def add_new_invoice():
#     # DATE VALUE CURRENCY PAYMENT_VALUE(?)
#     temp = [enter_date(), enter_amount(), enter_currency(), 0]
#     INVOICES.append(temp)
#     print(INVOICES)

def add_new_invoice():
    # DATE VALUE CURRENCY PAYMENT_VALUE(?)
    file = open(m_file, 'a', newline='')
    writer = csv.writer(file)
    date = str(enter_date())
    amount = str(enter_amount())
    currency = str(enter_currency())
    writer.writerow([date,amount,currency])
    file.close()

def add_new_payment():
    pass

def view_payments():
    pass

m_userMenu = {
    1: ["Add new invoice", add_new_invoice], 
    2: ["View all invoices", show_all_invoices],
    3: ["Add new payment",add_new_payment],
    4: ["View payments",]
}


    

# MAIN LOOP
while True:
    # print main menu
    for option in m_userMenu: 
        print(str(option) + ".", m_userMenu[option][0])
# get option from user
    selection = int(input("Select option: "))
    m_userMenu[selection][1]()
