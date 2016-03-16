# FluxLight
Controls a cheap RGB Wifi Lightbulb to mimick the color temperature changing patterns of f.lux, using python3.

### Usage
This is only intended for use with the [MagicLight Wifi LED Lightbulb](http://www.amazon.com/MagicLight%C2%AE-WiFi-LED-Light-Bulb/dp/B00SIDVZSW). For this purpose it is independent of the Anroid/iOS application; you will still need the app for configuration and regular use.
  
1. Configure your lightbulb to connect to your local network using the provided app.
2. Go to settings and find the ip address of your lightbulb. (Scanning with Nmap works too, I found ports 80 and 5577 were open and the MAC Address OUI was AC:CF:23 (Hi-flying electronics technology))
3. In FluxLight.py, edit the value of light.IP to match your IP address. You can also adjust the maximum and minimum color temperatures.
4. Run the code in python3.

### Background
I heard about a brand of "smart bulbs" that were releasing a version that could tint to different shades of white. After seeing the cost, I figured that the same thing could be done with a cheaper bulb that also supports full RGB color.

I set up my laptop as an access point, and with wireshark I was able to capture all of the data being sent to and from the bulb. I noticed a pattern and was able to send data back from my computer, circumventing the use of the offical app (closed source). I encountered some difficulty trying to understand the structure of the data being sent, as there were a few "magic bytes" that remained constant and what appeared to be a 1 byte checksum value. In the end, I got around this value by brute forcing all of the values that this could be. By no means is this elegant or the best solution, however considering the scale of this project, it made the most sense. (I'm only using this on one bulb, updated every 30 minutes.)

Once I was able to control the bulb, the next steps were to convert Kelvin to RGB and write a sinusoidal function that would produce warm colors at night and cool colors during the day. This part was inspired by the software [f.lux](https://justgetflux.com/). I used [this writeup](http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/) to generate the RGB values.

After some experimenting, I noticed that my bulb was tinting all of the colors very blue, so I calibrated #FFFFFF until I thought it looked right. This calibration can be seen in Lightbulb.py.

## Credit
[TannerHelland.com for the K to RGB algorithm](http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/)

Chris Johnston 2016
