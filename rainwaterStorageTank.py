#introduction

print("Welcome to the rainwater tank calculator.")
print("We'll ask for a few parameters about your rainfall and rain catchment area.")
print("Then, we'll tell you how big to make your tank.")
print("We assume that your catchment area is rectangular")
print("")

#grab input from the player

rainfall = float(input("How many inches of rainfall in a large storm? "))
wide = float(input("How wide is your catchment area, in feet? "))
long = float(input("How long is your catchment area, in feet? "))

#convert units

new_rainfall = (rainfall) / 12
volume = new_rainfall * wide * long
result = (volume*7.48)

#round

round(result/0.5)

#print results

print("")
print("You need a tank with", result, "gallons capacity to capture that much rain at one time.")