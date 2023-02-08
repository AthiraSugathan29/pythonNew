# Write a Python program to convert a dictionary of Celsius temperatures into Fahrenheit.
celsius = {'t1': 35,'t2': 36.5,'t3': 35.8,'t4': 37.5}
# Get the corresponding "fahrenheit" values and create the new dictionary
fahrenheit = {key:(value * 1.8) + 32 for (key,value) in celsius.items()}
print(fahrenheit)
