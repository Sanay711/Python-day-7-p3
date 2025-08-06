print("Select your ride: ")
print("1. 🛞🛞Two Wheeler")
print("2. 🚗Car")
choice = int( input("Enter your 1st choice: ") )
 
if( choice == 1 ): 
  print( "What type of bike would you like to ride in? " )
  print("1. 🚵🏻Bike\n")
  print("2. 🛵Scooter\n")

  
  choice2=int(input("Enter your 2nd choice: "))
  if choice2==1: 
    print("You have selected a bike.")
  else:
    print("You have selected a scooter")


elif( choice == 2 ): 
  print( "What type of car would you like to ride in?" )
  print("1. 🚗Sedan")
  print("2. 🚙SUV(Sports Utility Vehicle)")
  choice3=int(input("Enter your 3rd Choice: "))
  if choice3==1: 
    print("You have selected a Sedan")
  else:
    print("You have selected an SUV")

else:
  print("Wrong choice!")