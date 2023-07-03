import math

#Integer only inputs taken from https://www.101computing.net/number-only/ .
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))    
    except ValueError:
       print("Please enter an integer.")
       continue
    else:
       return userInput 
       break 

#Start a while loop so user can retry if they enter invalid info.
while True:

    #Allows the user to choose which type of calculator they wish to use.
    print("Investment - Calculates the amount of interest earned annually on your investments")
    print("Home Loan - Calculates amount you will have to repay on your mortgage each month")

    calc_choice = input("\nEnter 'investment' or 'home' to choose the calculator you wish to use: ")

    calc_choice = calc_choice.lower().strip(" ")

    #Proceed to investment calculator.
    if calc_choice == "investment":
        print("You have selected Investment calculator")
        
        amount = inputNumber("Please enter the amount you wish to invest: ")

        interest_rate = inputNumber("Please enter the interest rate: ")
        interest_rate = (interest_rate / 100)

        years = inputNumber("How many years do you plan to invest for: ")

        interest = " "
        while interest != "yes" or "no":
            interest = input("Type 'Yes' for Compound Interest, 'No' for Simple Interest): ")
            interest = interest.lower().strip(" ")
            
            #Uses compound interest formula to calculate.
            if interest == "yes":
                total = amount * math.pow((1 + interest_rate), years)
                #Used https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/ to help with formatting for 2 decimal places since we are working with currency.
                print("Your investment will be worth £" "%.2f"  % total)
                break
            #Uses simple interest formula to calculate. 
            elif interest == "no":
                total = amount * (1 + interest_rate * years)
                print("Your investment will be worth £" "%.2f"  % total)
                break
    
            #Ask user to try again and enter a valid choice.
            else:
                print("Error: You have entered an invalid choice.")
        break

    #Proceed to home calculator.
    elif calc_choice == "home":
        print("You have selected Home Loan calculator")

        house_value = inputNumber("Please enter the current house value: ")

        interest_rate = inputNumber("Please enter the interest rate: ")
        interest_rate = (interest_rate / 100)
        monthly_interest = (interest_rate / 12)

        months = inputNumber("How long do you plan to repay the loan for (in months): ")

        #Calculate total using bond repayment formula.
        total = (monthly_interest * house_value) / (1 - (1 + monthly_interest)**(-months))
        print("Your monthly mortgage repayment will be £" "%.2f" % total)
        break


    else:
        print("Error: You have entered an invalid choice, please try again")