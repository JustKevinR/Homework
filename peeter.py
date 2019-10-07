name = input("Sisesta enda nimi: ")
b = name.capitalize()
print ("Tere " + b)
place = input("Sisesta enda elukoht: ")
a = place.casefold()
if a=="saaremaa":
    print("Tere saarlane")
age = int(input("Sisesta enda vanus: "))
if age == 18:
    print ("Õnnitlused täisealise puhul")
if age >=18:
    print ("Võid autot juhtida")
elif age <=18:
    print ("Liiga noor, et autot juhtida")
