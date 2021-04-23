import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

print("{0:12}{1}".format("investment","- to calculate the amount of interest you'll earn on interest"))
print("{0:12}{1}".format("bond","- to calculate the amount you'll have to pay on a home loan\n" ))

#prompt the user for the choice

choice = input()

if choice == "investment" or choice == "Investment" or choice == "INVESTMENT":
    #initialize the variable to be used for the formulaes
    
    P = float(input("How much money are you depositing?: \n"))
    i = float(input("What is the current interest rate as a percentage?:(enter a digit only) \n"))
    t = float(input("How many years do you plan on investing?: \n"))
    interest = input("Do you want 'simple' or 'compound' interest?: \n")
    r = i / 100
    #make the answer not case sensitive any choice of case should not matter
    
    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        total = P*(1 + r * t)
        print("Your total amount once simple interest has been applied is: \nR",round(total,2))
        
    #offer the choice of the full word "simple interest" incase user used it
    elif interest == "simple interest" or interest == "Simple interest" or interest == "SIMPLE INTEREST" or interest == "Simple Interest":
        total = P*(1 + r * t)
        print("Your total amount once simple interest has been applied is: \nR",round(total,2))
    elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":
        total = P * math.pow(1 +r , t)
        print("Your total once compound interest has been applied is: \nR",round(total, 2))
    elif interest == "compound interest" or interest == "Compound interest" or interest == "Compound Interest" or interest == "COMPOUND INTEREST":
        total = P * math.pow(1 +r , t)
        print("Your total once compound interest has been applied is: \nR",round(total, 2))
        
    #any other input is invalid, display appropriate message
    else:
        print("You have entered something invalid.")

elif choice == "bond" or choice == "BOND" or choice == "Bond":
    P = float(input("Please enter the present value of the house: \n"))
    I = float(input("What is the the current interest rate?: (enter a digit only)\n"))
    n = float(input("how many months do you plan to take to repay the bond?:\n"))
    i = I / 12
    repayment = (i*P)/( 1 - (1+i)**(-n))
    print("Your total bond repayment per month is: \nR",round(repayment,2))

#check that the user doesn't enter an empty input and display appropriate message
elif choice == "":
    print("You haven't entered anything")

#if the user has entered an invalid, non empty input print appropriate message
else:
    print("You have entered an invalid choice.")
