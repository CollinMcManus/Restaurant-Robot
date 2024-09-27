#Robot Order Project!
print()
print("Hello, welcome to Collin's Sandwich Shop, I am your personal robot server Rob T.\n")

print("To whom do I have the pleasure of serving?\n")
name = input()
print()
print("Hello " + name + ", thank you for deciding to eat at the best cafe in town!\n")

Menu = ("	 			Collin's Sandwich Shop Sandwiches\n\nPlease make a selection below\n\n	Chicken $12\n	Beef $14\n	Lamb 15$\n	Salmon $16")

print(Menu + "\n\nHere is our menu of delectable sandwiches, would you like to place your order now?")
print()
yes = input()

print_message = False
if yes == "yes" or yes == "Yes" or yes == "Y" or yes == "y" or yes == "sure" or yes == "Sure" or yes == "please":
		print_message = True
else:
	print("\nNo worries, please take your time, I'll be back in a moment\n")
	while True:
		pause_input = input("Please select Enter when you are ready to order...")
		if pause_input == "":
			print_message = True
			break


if print_message:
	print("\nGreat, what did you decide on?\n")

	valid = ["chicken", "beef", "lamb", "salmon"]

	while True:
			selection = input().lower()
			if selection in valid:
				break
			else:
				print("I am so sorry, we do not have " + selection + " on the menu. Please choose from one of our delicious sandwiches.\n")

if selection == "lamb" or selection == "beef":
	while True:
		temperature = input("\nOh that's a great choice, What temperature would you like for your " + selection + "\n") + " "
		break
elif selection == "salmon":
	print("\nOh, I believe you will love our salmon, the sandwich includes a creamy dill sauce!")
	while True:
		temperature = ('')
		break
elif selection == "chicken":
	print("\nThe chicken is grilled with specially selected spices and herbs that I believe you will enjoy!")
	while True:
		temperature = ('')
		break
#
print("\nPerfect " + name + ", I will let the Chef know and your " + temperature + "" + selection + " will be ready shortly! :)")
while True:
    bill = input("\nHit Enter when you are ready to receive the bill...\n")
    if bill == "":
        break
		
if selection == "salmon":
	print("that will be $16")
elif selection == "lamb":
	print("That will be $15")
elif selection == "beef":
	print("That will be $14")
elif selection == "chicken":
	print("That will be $12")
print("\nThank you for dining with us, if you've enjoyed your meal please feel free to leave a comment by scanning the QR code at the bottom of your bill.")