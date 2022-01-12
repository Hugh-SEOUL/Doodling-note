appleQuality = input("The quality of an apple(Fresh, rotten) : ")


if appleQuality == "Fresh" :
    applePrice = int(input("The price of an apple : "))
    if applePrice < 1000 : 
        print("purchase 10 apples")
    else:
        print("purchase 5 apples")
else:
    print("Do not purchase")
    