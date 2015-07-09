//---bof---RGBL-Analog Preamble

//RGB LED pins
int ledAnalogOne[] = {3, 5, 6}; //the three pins of the first analog LED 3 = redPin, 5 = greenPin, 6 = bluePin
                                //These pins must be PWM
                                
                                
//Defined Colors (different RGB (red, green, blue) values for colors
//(to add your own ie. fuscia experiment and then add to the list) 
byte oldColor[] = {};
byte newColor[] = {};

 
                              
void setup(){
  for(int i = 0; i < 3; i++){
   pinMode(ledAnalogOne[i], OUTPUT);   //Set the three LED pins as outputs
   }
   byte BLACK[] = {0, 0, 0}; 
   setColor(ledAnalogOne, BLACK);       //Turn off led 1
   
   Serial.begin(9600);
   
    
}

  
  
void loop(){
   if (Serial.available() > 0) {
     // Setting oldColour
    oldColor[0] = newColor[0];
    oldColor[1] = newColor[1];
    oldColor[2] = newColor[2];
    //Dealing with the serial input
    String myString = Serial.readStringUntil('\n');
    // Search for first comma
    int commaIndex = myString.indexOf(',');
    //  Search for the next comma just after the first
    int secondCommaIndex = myString.indexOf(',', commaIndex+1);
    //Set RGB values as strings
    String firstValue = myString.substring(0, commaIndex);
    String secondValue = myString.substring(commaIndex+1, secondCommaIndex);
    String thirdValue = myString.substring(secondCommaIndex+1); // To the end of the string
    //Changing the values to integers
    int r = firstValue.toInt();
    int g = secondValue.toInt();
    int b = thirdValue.toInt();
    //Setting the newColor
    newColor[0] = r;
    newColor[1] = g;
    newColor[2] = b;
   //Fading the colour
   fadeToColor(ledAnalogOne, oldColor, newColor, 20); 

  }
  
}


//Functions for programs


void setColor(int* led, byte* color){
 for(int i = 0; i < 3; i++){             //iterate through each of the three pins (red green blue)
   analogWrite(led[i], 255 - color[i]);  //set the analog output value of each pin to the input value (ie led[0] (red pin) to 255- color[0] (red input color)
                                         //we use 255 - the value because our RGB LED is common anode, this means a color is full on when we output analogWrite(pin, 0)
                                         //and off when we output analogWrite(pin, 255). 
 }
}


void fadeToColor(int* led, byte* startColor, byte* endColor, int fadeSpeed){
  int changeRed = endColor[0] - startColor[0];                            //the difference in the two colors for the red channel
  int changeGreen = endColor[1] - startColor[1];                          //the difference in the two colors for the green channel 
  int changeBlue = endColor[2] - startColor[2];                           //the difference in the two colors for the blue channel
  int steps = max(abs(changeRed),max(abs(changeGreen), abs(changeBlue))); //make the number of change steps the maximum channel change
  
  for(int i = 0 ; i < steps; i++){                                        //iterate for the channel with the maximum change
   byte newRed = startColor[0] + (i * changeRed / steps);                 //the newRed intensity dependant on the start intensity and the change determined above
   byte newGreen = startColor[1] + (i * changeGreen / steps);             //the newGreen intensity
   byte newBlue = startColor[2] + (i * changeBlue / steps);               //the newBlue intensity
   byte newColor[] = {newRed, newGreen, newBlue};                         //Define an RGB color array for the new color
   setColor(led, newColor);                                               //Set the LED to the calculated value
   delay(fadeSpeed);                                                      //Delay fadeSpeed milliseconds before going on to the next color
  }
  setColor(led, endColor);                                                //The LED should be at the endColor but set to endColor to avoid rounding errors
}


