# This code is intended for the MagicLight Wifi LED Lightbulb
# http://www.amazon.com/MagicLight%C2%AE-WiFi-LED-Light-Bulb/dp/B00SIDVZSW
# as seen here.

import socket
import binascii

IP = "192.168.2.37"
PORT = 5577

mode = "31" # "default" mode
magicBytes = "00f00f"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connect():
    try:
        s.connect((IP, PORT))
        print ("Connected to " + IP + ":" + str(PORT))
    except:
        print ("Failed to connect")

# adjust the calibration to fit your bulb. Mine was *very* blue w/ white light.
def calibrate(color):
    return (int(color[0] * 1), int(color[1] * 0.95), int(color[2] * 0.6))

# sends a (r,g,b) color to the lightbulb
def setColor(color):
    print("Sending color: " + str(color))
    color = calibrate(color)
    # the structure of the packets sent to the light are
    # pattern, red, green, blue, "00f00f", some 1 byte checksum?
    # I have yet to establish a pattern between the colors and the checksum
    # but since it's only 255 bytes, I don't think it's too big a deal.
    for x in range(255):
        message = mode + format(color[0], "02x") + format(color[1], "02x") + format(color[2], "02x") + magicBytes + format(x, "02x")
        s.send(bytes.fromhex(message))
