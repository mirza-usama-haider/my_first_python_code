#---------------------------------------------------------------------------------
#age= 22
#first_name="Mirza"
#is_alive = False

#print(age)

#print("Hello, World!")

#first_name = "John"
#last_name= "Smith"
#age = 20
#is_registered =  False

#name = input("What is your name? ")
#print("Hello "+ name +" Are you happy with it? ")
#------------------------------------------------------------------------------------

#birth_year = input("What is your birth year ? ")
#age = 2021 - int(birth_year)
#print(age)

##---------------------------------------------------ADD----------
#################
#
#str()
#bool()
#int()
#float()
#
#################



#first_number = input("First Number: ")

#second_number = input("Second Number: ")

#sum = float(first_number) + float(second_number)

#print("Sum: " + str(sum))

#---------------------------------------------------------------

#motto = "Life is Short"

#print(motto.upper())

#print(motto.lower())

#print(motto.find("Life"))

#print(motto.find("Happiness"))

#print(motto.replace("Short","Full of Suffering"))

#print("Life"  in motto)

#print("Happiness"  in motto)

#---------------------------------------------------------------


#---------------Weight conversion----------------------------------

weight = input("Weight: ")
weight = float(weight)
choice = input("Kg or Lb: ")

if choice == 'k' or choice == 'K':
    weight *= 2.2046
    print("Weight in Lb : " + str(weight))
elif choice == 'l' or choice == 'L':
    weight /=2.2046
    print("Weight in Kg : " + str(weight))

