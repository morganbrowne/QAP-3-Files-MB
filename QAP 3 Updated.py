# Name: Morgan Browne
# Date(s) Feb 10-13, 24
# Updates: April 14th - Put Validations in inputs. 

#Discription: Keep Track OF Car Sales At Dealership 

# Enter Inputs 


import datetime
import re


while True: 
    #Gather user input
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
    while True: 
        FirstName = input("Enter the custommers first name (END to quit): ").title()
        if FirstName.upper() == "END":
            break

        if FirstName == "":
            print("Data Entry Error - Customr First Name Cannot Be Blank.")
        else:
            break
    if FirstName.upper() == "END":
        break
    print("Continue with the program.")

   
    while True:
        LastName = input("Enter the customer's last name: ").title()
        if LastName == "":
            print("Data Entry Error - Customer Last Name Cannot Be Blank.")
        elif not LastName.isalpha():
            print("Data Entry Error - Last Name Cannot Contain Numbers.")   
        else:
            break

    
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    while True:
        Prov = input("Enter the customer province (XX): ")
        if Prov == "":
            print("Error - cannot be blank.")
        elif len(Prov) != 2:
            print("Error - must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Error - invalid province.")
        else:
            break


    while True:
        City = input("Enter the customer's City: ").title()
        if City == "":
            print("Data Entry Error - City Cannot Be Blank.")
        elif not City.isalpha(): # This is so the user cannot enter numbers, only problem is the city wont be able to have punctuation marks.
            print("Data Entry Error - City Cannot Contain Numbers.")
        else:
            break

    while True:
        Address = input("Enter the customer's Address: ").title()
        if Address == "":
            print("Data Entry Error - Address Cannot Be Blank.")
        else:
            break

    while True:
        PostCode = input("Enter the customer's Postal Code (A1A A1A): ").upper()
        
        # Check if the postal code is blank
        if PostCode == "":
            print("Data Entry Error - Postal Code Cannot Be Blank.")
            continue
        
        # Define a regular expression pattern for Canadian postal codes (A1A 1A1)
        pattern = r'^[A-Z]\d[A-Z] \d[A-Z]\d$'
        
        # Validate the format of the postal code
        if not re.match(pattern, PostCode):
            print("Data Entry Error - Invalid Postal Code Format. Please use format A1A 1A1.")
            continue
        
        # If the code passes all validations, break the loop
        break
        
    while True:
        PhoneNum = input("Enter your phone number (format: XXX-XXXX): ")

        # Regular expression to match the format XXX-XXXX
        pattern = re.compile(r'^\d{3}-\d{4}$')

        if pattern.match(PhoneNum):
            # Removing non-numeric characters for counting digits
            cleaned_number = ''.join(filter(str.isdigit, PhoneNum))
            if len(cleaned_number) == 7:
                print("Valid phone number.")
                break  # Exit the loop since a valid phone number is entered
            else:
                print("Invalid phone number. Please enter a phone number with 7 digits after the hyphen.")
        else:
            print("Invalid phone number format. Please enter in the format XXX-XXXX.")
    
   

    while True:
        PlateNum = input("Enter the customer's plate number (XXX999): ").upper()
        if PlateNum == "":
            print("Data Entry Error - plate number cannot be blank.")
        elif not re.match(r'^[A-Z]{3}\d{3}$', PlateNum):
            print("Data Entry Error - Invalid plate number format. Plate number must be in the format XXX999.")
        else:
            break

    
    while True:
        CarMake = input("Enter the car make: ").title()
        if CarMake == "":
            print("Data Entry Error - car make cannot be blank.")
        else:
            break
        
    while True:
        CarModel = input("Enter the car model: ").title()
        if CarModel == "":
            print("Data Entry Error - car model cannot be blank.")
        else:
            break
    while True:
        try:
            CarYear = int(input('Enter the year of the car: '))
            if CarYear in range(1000, 10000):
                break

        except:
            print("Data Enter Error - Car year must only be 4 didgits. ")
        else:
            break

    while True:
        SellPrice = input("Enter the sales price of the car: ")
        SellPrice =int(SellPrice)
        if SellPrice > 50000:
            print("Data Entry Error - sales price of the car must not be over $50000. ")
        else:
            break

    while True:
        TradePrice = input("Enter the trade in  price of the car: ")
        TradePrice = int(TradePrice)
        if TradePrice > SellPrice:
            print("Data Entry Error - Trade in value of the car must not exed the sale values of car. ")
        else:
            break
        
    while True:
        SalesPerson = input("Enter the Salesman name: ").title()
        if SalesPerson == "":
            print("Data Entry Error - Salesman Name Cannot Be Blank.")
        else:
            break

print("You ended the program.")
# Constants

HST_RATE = 0.15
LUX_TAX = 0
CUR_DATE = datetime.datetime.now()
FIANCE_FEE = 39.99

# Calculations

AftPriceTrade = SellPrice - TradePrice 

if SellPrice > 5000.00:
    LiceFee = 75.00
elif SellPrice < 5000.00:
    LiceFee = 165.00

TransFee = 0.01 * AftPriceTrade

if SellPrice < 20000.00:
    LUX_TAX = 0.16 * SellPrice

SubTot = AftPriceTrade + LiceFee + TransFee + LUX_TAX
HST = HST_RATE * SubTot
TotSalePrice = HST + SubTot

PayDate = CUR_DATE + datetime.timedelta(days=30)

# Print Results 
print()
print()
CUR_DATEDsp = datetime.datetime.strftime(CUR_DATE, "%m-%d-%Y")
print(f"Honest Harry Car Sales                       Invoice Date: {CUR_DATEDsp}")
print(f"Used Car Sale and Receipt                    Receipt No: {FirstName[0]}{LastName[0]}-{PlateNum[3:6]}-{PhoneNum[6:10]}     ")
print()
SellPriceDsp = "${:,.2f}".format(SellPrice)
print(f"                                        Sale price:        {f'${SellPrice:,.2f}':<9s}")
TradePriceDsp = "${:,.2f}".format(TradePrice)
print(f"Sold to:                                Trade Allowance:   {f'${TradePrice:,.2f}':<9s}") 
print(f"                                        -----------------------------------")
AftPriceTradeDsp = "${:,.2f}".format(AftPriceTrade)
print(f"   {FirstName[0]}, {LastName:<27s}       Price after trade: {f'${AftPriceTrade:,.2f}':<9s}")
LiceFeeDsp = "${:,.2f}".format(LiceFee)
print(f"   {Address:<8s}                         Licence Fee:       {f'${LiceFee:,.2f}':<6s}")
TransFeeDsp = "${:,.2f}".format(TransFee)
print(f"  {City:<6s}, {Prov:<2s} {PostCode:<6s}                    Transfer Fee:      {f'${TransFee:,.2f}':<7s}")
print(f"                                        ------------------------------------")
SubTotDsp = "${:,.2f}".format(SubTot)
print(f"Car Details:                            Subtotal:          {f'${SubTot:,.2f}':<9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"                                        HST:               {f'${HST:,.2f}':<9s}")
print(f"   {CarYear:<4d} {CarMake:<6s} {CarModel:<6s}                   ------------------------------------")
TotSalePriceDsp = "${:,.2f}".format(TotSalePrice)
print(f"                                        Total sales price: {f'${TotSalePrice:,.2f}':<9s}")
print(f"-------------------------------------------------------------------------------")
print()
print(f"                                     Financing         Total         Monthly ")
print(f"    # Years       # Payments            Fee            Price         Payment ")
print(f"   -------------------------------------------------------------------------")
for Years in range(1, 5):

    MonPayMent = TotSalePrice / (Years * 12)
    TotPrice = TotSalePrice + FIANCE_FEE + MonPayMent
    NumPay = Years * 12
    FineFee = FIANCE_FEE * Years

    NumPayDsp = "${:,.2f}".format(NumPay)
    FIANCE_FEEdsp = "${:,.2f}".format(FIANCE_FEE)
    TotPriceDsp = "${:,.2f}".format(TotPrice)
    MonPayMentDsp = "${:,.2f}".format(MonPayMent)

    print(f"     {Years:>2d}            {NumPay:>3d}             {f'${FineFee:,.2f}':>9s}       {f'${TotPrice:,.2f}':>9s}      {f'${MonPayMent:,.2f}':>9s}")
print(f"   -------------------------------------------------------------------------")
PayStart = CUR_DATE + datetime.timedelta(days=30)
CUR_DATEDsp = datetime.datetime.strftime(CUR_DATE, "%d-%m-%y")
PayDateDsp = datetime.datetime.strftime(PayDate, "%d-%m-%y")
print(F"   Invoice Date {CUR_DATEDsp}                              First Payment {PayDateDsp}      ")
print()
print(f"-------------------------------------------------------------------------------")
print(f"                       Best used cars at the best prices!")



