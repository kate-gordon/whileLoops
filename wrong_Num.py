#Blastoff 4
#Now, make sure the user doesn't enter a number larger than 20

y = True   
while y:
    x = int(input("Where to start? "))
    if x <= 20:
        while x > 0:
            print(x)
            x -= 1 
    else:
        print ("Oops! That number is too big")
        continue
    y = False
        