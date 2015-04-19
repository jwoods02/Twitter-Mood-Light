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

### Step 1

Install Twitter API and pySerial libraries onto your computer. 

### Step 2

Set up the analog one RGB LED as shown in the breadboard diagram in [this](http://oomlout.com/parts/LEDF-10-RGB-03-guide.pdf} guide

### Step 3

Change the <insert serial port here> on line 25 in the python file to the Serial port of your Arduino which can be found here.

### Step 4 

Get your details for the Twitter API by following the instructions here and insert them into lines 31 to 34 in the Python file.

### Step 5

To start the program first plug in the USB cable and compile the Arduino program to the Arduino board, then start the Python program and you should see the LED change colours (usually green) then every 5 seconds you should see a subtle colour change. The project is working. 

Note: The program will only work if the Python program is running on the PC and the USB cable is plugged into the Arduino.
