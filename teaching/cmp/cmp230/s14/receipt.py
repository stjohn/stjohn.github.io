#Test program for the receipt question for S 13

def main():
    priceList = eval(input("Enter: "))
    total = 0
    for price in priceList:
        print("       {0:6,.2f}".format(price))
        total = total + price
    print("----------------")
    print("Total: {0:6,.2f}".format(total)) 

main()
