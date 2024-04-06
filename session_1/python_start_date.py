input = input("What is the python start date?\n")
if(input == "1991"):
    print("You are correct.")
else:
    if(input=="1990" or input=="1992"):
        print("You are too close to correct answer.")
    else: 
        print("Wrong Answer")
print("Thank you for you participation!!!")