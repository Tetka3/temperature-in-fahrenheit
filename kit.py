temp = input("Enter a temperature in Celcius ")
temperature = float(temp)
if temperature<-273.15:
    print("The temprature is invalid because it is below absolute zero")
elif temperature==-273.15:
    print("The temperature is absolute 0")
elif temperature>0:
    print("The temperature is below freezing point")
elif temperature==0:
    print("The temperature is at freezing point")
elif temperature>100:
    print("The temperature is in normal range")
elif temperature==100:
    print("The temperature is at boiling point")
else: 
    print("The temperature is above the boiling point")