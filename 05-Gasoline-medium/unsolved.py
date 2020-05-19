# You can find these measures on the web (try wikipedia), but just in case:
# • 1 gallon is equivalent to 3.7854 liters
# • 1 barrel of oil produces 19.5 gallons of gas (approximately, can vary depending on the oil
# source. This number will work for us). FYI, a barrel is 42 gallons.
# • 1 gallon of gas produces approximately 20 pounds of CO2. Again, good enough
# • 1 gallon of gas produces 115,000 BTU (British Thermal Units). 1 gallon of ethanol
# produces 75,700 BTU.
# • God knows what the cost should be, but let’s peg it at $4.00/gallon
# Neçə litr edir?
#Neçə barel edri?
#CO2-nin miqdarı nə qədərdir?
#Etanol gallonun enerji qarşılığı nə qədərdir?
#Dollar ilə qiyməti nə qədərdir?
galloninput=int(input('nece gallon?:'))
print('Neçə litr edir?:',galloninput*3.7854)
print('Neçə barel edri?:',galloninput*19.5)
print('CO2-nin miqdarı nə qədərdir?:',galloninput*3.7854*20)
print('Etanol gallonun enerji qarşılığı nə qədərdir?:',galloninput*3.7854*115,000*75,700)
print('Dollar ilə qiyməti nə qədərdir?:',galloninput*4)