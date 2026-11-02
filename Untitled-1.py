def calc_electricitybill(amount,units,rates,tax_rate,finalamount,ebill):
    units=int(input("Enter the units: "))
    amount=int(input("Enter amount: "))
    if(units>1 and units<=100):
        rates=5
        ebill=units*rates
        print("Electricity bill before additional charge: ",ebill)
        tax_rate=0.05 # additional charges
        finalamount=ebill+ebill*tax_rate
        print("Electricity bill after additional charge: ",finalamount)
    elif(units>100 and units<=200):
        rates=7
        ebill=units*rates
        print("Electricity bill before additional charge: ",ebill)
        tax_rate=0.1 # additional charges
        finalamount=ebill+ebill*tax_rate
        print("Electricity bill after additional charge:",finalamount)
    elif(units>200 and units<=300):
            rates=10
            ebill=units*rates
            print("Electricity bill before additional charge: ",ebill)
            tax_rate=0.2 # additional chargres
            finalamount=ebill+ebill*tax_rate
            print("Electricity bill after additional charge:",finalamount)
    else:
        print("Invalid units")
calc_electricitybill(0,0,0,0,0,0)
        


