# Temperature Converter
#
# Filename: temperature-converter
# Author:   Javad Tehrani
# Date:     2025-02-28

# Function temperature converter
def temperature_converter (temp, unit):
    # If Celsius then
    if (unit.upper() == "C"):

        #   Fahrenheit is Celsius * 9 / 5 + 32
        converted_temperature = temp * 9 / 5 + 32

    # Else
    else:
        # Celsius is (Fahrenheit -32) * 5 / 9
        converted_temperature = (temp - 32) * 5 / 9
    # End if
    return converted_temperature

# Function Scale Converter
def scale_converter (unit):
    if (unit == "C"):
        converted_scale = "F"
    else:
        converted_scale = "C"
    return converted_scale

# Ask for the temperature
temperature = float(input("Temperature\n"))


# Ask for the scale (Celsius, Fahrenheit)
scale = input("Celsius (C) or Fahrenheit (F): \n")
scale = scale.upper()

converted_temperature = temperature_converter(temperature, scale)

converted_scale = scale_converter(scale)

# Display Converted Temperature


print(temperature, scale, "is ", converted_temperature, converted_scale)


