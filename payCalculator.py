def calculatePay():
    # Implement your solution in between the two comment blocks
    
    # This first line is provided for you

    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    pay = float(hrs)*float(rate)
    print("Enter Hours:" +" "+ hrs)
    print("Enter Rate:" +" "+ rate)
    print(pay)
    
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()