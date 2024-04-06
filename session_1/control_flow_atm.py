balance = 10000
pin = 1234

get_pin = int(input("Enter your pin please: "))

if(pin==get_pin):
    print("Your current balance is:",balance)
    get_decision= input("Would you like to deposit or withdraw some money? \n 1.Deposit\n 2.Withdraw\n 3.None\n")

    if(get_decision=="1"):
        d_amount = int(input("How much you want to deposit?\n Deposit Amount: "))
        balance+=d_amount
    elif(get_decision=="2"):
        w_amount= int(input("How much you want to withdraw?\n Withdraw Amount: "))
        if(abs(w_amount-balance)>=500):
            balance-=w_amount
        else:
            print("You have to keep at least 500 in your account.")
    
    print("Your current balance is:",balance)
else:
    print("Please write the correct pin!!!")