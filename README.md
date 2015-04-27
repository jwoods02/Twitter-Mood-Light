# Twitter Mood Light

An Arduino and Python project that shows the mood of Twitter as an RGB LED.

## Instructions

### Things you Will Need

Arduino Uno w/ USB Cable and Breadboard

RGB LED

Resistor

3 Jumper Cables

Python 3.4

Arduino IDE

The RGB, Resistor and jumper cables I use can be bought in a package [here](http://oomlout.co.uk/collections/extra-pieces/products/frosted-leds-10mm-rgb-x3)

### Step 1

Install [Twitter API](https://github.com/geduldig/TwitterAPI) and [pySerial](http://pyserial.sourceforge.net/) libraries onto your computer. 

A guide to installing Python libraries can be found [here](https://docs.python.org/3/installing/)

### Step 2

Set up the analog one RGB LED as shown in the breadboard diagram in [this](http://oomlout.com/parts/LEDF-10-RGB-03-guide.pdf) guide

### Step 3

Change the <insert serial port here> on line 25 in the python file to the Serial port of your Arduino which can be found here.

### Step 4 

Get your details for the Twitter API by following the instructions [here](https://twittercommunity.com/t/how-to-get-my-api-key/7033) and insert them into lines 31 to 34 in the Python file.

### Step 5

To start the program first plug in the USB cable and compile the Arduino program to the Arduino board, then start the Python program and you should see the LED change colours (usually green) then every 5 seconds you should see a subtle colour change. The project is working. 

### Note
The program will only work if the Python program is running on the PC and the USB cable is plugged into the Arduino.
