import API
import csv
# Maybe work only on csv file instead of arrays?
INVOICES = []

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
           
        return amount
    
def enter_currency():
    currency = input("Enter currency name: ").upper()
    # TO DO: handle incorrect currency name
    return currency

def show_all_invoices():
    for invoice in INVOICES:
        print(f'DATE: {invoice[0]} VALUE: {invoice[1]} CURRENCY: {invoice[2]}')

# Invoice data
# def add_new_invoice():
#     # DATE VALUE CURRENCY PAYMENT_VALUE(?)
#     temp = [enter_date(), enter_amount(), enter_currency(), 0]
#     INVOICES.append(temp)
#     print(INVOICES)

def add_new_invoice(file):
    # DATE VALUE CURRENCY PAYMENT_VALUE(?)
    file["INVOICE DATE"].append(enter_date())
    file["INVOICE VALUE"].append(enter_amount())
    file["INVOICE CURRENCY"].append(enter_currency())
    # temp = [enter_date(), enter_amount(), enter_currency(), 0]
    # INVOICES.append(temp)
    # print(INVOICES)

def add_new_payment():
    pass

m_userMenu = {
    1: ["Add new invoice", add_new_invoice], 
    2: ["View all invoices", show_all_invoices],
    3: ["Add new payment",add_new_payment],
    4: ["View payments",]
}

file = open("INVOICES.xlsx", 'w')
reader = csv.DictReader(file)
add_new_invoice(reader)
    

# MAIN LOOP
# while True:
#     for option in m_userMenu: 
#         print(str(option) + ".", m_userMenu[option][0])

#     selection = int(input("Select option: "))
#     m_userMenu[selection][1]()
