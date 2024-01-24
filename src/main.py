import datetime
def wprowadz_kwote():
    while True:
            kwota= float(input("Wprowadź kwotę"))
            if kwota < 0:
                print("kwota nie może być ujemna")
            else:
                return kwota
            
def wprowadz_walute():
    return input("Wprowadź kod waluty")
def wprowadz_date():
    while True
        data_str=input("Wprowadz datę faktury  (RRRR-MM-DD):")
        data=datetime.datetime.strptime(data_str, '&Y-%m-%d')
     return data
