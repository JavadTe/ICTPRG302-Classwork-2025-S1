# Temperature Converter
#
# Filename: temperature-converter
# Author:   Javad Tehrani
# Date:     2025-02-28


# C to F => C*9/5+32
# F to C => (F-32) * 5 / 9
# C to K => C + 273.16
# K to C => K - 273.16
# F to K => ( F to C ) + 273.16
# K to F => Cto f ( K to C )


# Function temperature converter
def temperature_converter (temp, unit):
    # If Celsius then
    if scale_from == "C" and scale_to == "F":

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
scale_from = input("Celsius (C), Fahrenheit (F) or kelvin (K): \n")
scale_from = scale_from.upper()

# Ask for the scale (Celsius, Fahrenheit)
scale_to = input("Celsius (C), Fahrenheit (F) or kelvin (K): \n")
scale_to = scale_to.upper()

converted_temperature = temperature_converter(temperature, scale)

converted_scale = scale_converter(scale)

# Display Converted Temperature


print(temperature, scale, "is ", converted_temperature, converted_scale)


