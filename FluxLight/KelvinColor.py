import math

# http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
# convert temperature in K to RGB value
# intended for kelvin values between 1000 and 40,000 K
# returns a tuple of (Red, Green, Blue) values
def toRGB(tempK):
    tempK = tempK / 100

    red = 0
    green = 0
    blue = 0

    # calculate red
    if tempK <= 66:
        red = 255
    else:
        red = tempK - 60
        # magic numbers, from tannerhelland.com
        red = 329.698727446 * math.pow(red , -0.1332047592)
        red = clamp(red, 0, 255)

    # calculate green
    if tempK <= 66:
        green = 99.4708025861 * math.log(tempK) - 161.1195681661
    else:
        green = tempK - 60
        green = 288.1221685283 * math.pow(green , -0.0755148492)
    green = clamp(green, 0, 255)

    # calculate blue
    if tempK >= 66:
        blue = 255
    else:
        if tempK <= 19:
            blue = 0
        else:
            blue = tempK - 10
            blue = 138.5177312231 * math.log(blue) - 305.0447927307
            blue = clamp(blue, 0, 255)

    return (red, green, blue)

def clamp(value, small, large):
    return int(max(small, min(value, large)))

#def printRGB(tuple):
#    print(tuple, sep = " ")