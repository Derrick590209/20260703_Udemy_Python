# program ask user's name
# cash
# Y(餓)/N
# program checks if the user has more than or equal to 30

name = input("Enter your name:") # string
money = int(input("Enter your cash amount:"))
hungry = input("Are you hungry?(Y/N)")
if hungry == "Y":
    if money >= 30:
        print(f"{name} should go to eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enought money to eat breakfast.")
        
elif hungry == "N":
    if money >= 30:
        print(f"{name} has budget but dosen't want to go to eat breakfast.")
    else:
        print(f"{name} has no money and not hungry.")

else:
    print("Please make sure that you enter either Y or N.")




