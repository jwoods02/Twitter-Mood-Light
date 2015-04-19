import time
import csv
import serial
from TwitterAPI import TwitterAPI

# [angry, happy, sad]
emotion = [0,0,0]

# [R,G,B]
colour = [0,0,0]

# number of times colour has been logged
count = 0

# delay between each log
delay = 5

# sets timer
timeout = time.time() + delay
 
#Boolean value for if Arduino is connected
connected = False

#Serial connection setup
ser = serial.Serial("<insert serial port here>", 9600)

# Twitter API setup
TRACK_TERM = ':@, :/, :), :('

# KEEP SECRET
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)

# Emotion algorithm
def whatColor():
    global emotion
    totalNum = sum(emotion) # number of tweets analysed
    for i in range(0, len(emotion)): # for each emotion count
        emotion[i] = (emotion[i]/totalNum)*255 # find proportion of that emotion as a franction of 255
        emotion[i] = round(emotion[i], 2) #round to 2 decimal places
        
        


#MAIN PROGRAM
r = api.request('statuses/filter', {'track': TRACK_TERM})

for item in r: # for each tweet
    if time.time() > timeout: # If time elapsed
        print("raw data emotion", emotion)
        whatColor()
        print('emotion', emotion)
        serialColour = ','.join(map(str,emotion))
        ser.write(serialColour.encode())
        print()# Line break for debugging
        colour = [0,0,0] # resets colour
        emotion = [0,0,0] # resets tweet count
        time.sleep(2) # 2 second delay...
        timeout = time.time() + delay #resets timer
        
    #Manipulates tweet to add to emotion counter    
    leitem = item['text'] if 'text' in item else item # select tweet text
    leitem = str(leitem).encode('utf-8') # encode it so python reconises it
    if (':@' or ':/') in str(leitem): # if tweet contains angry
        emotion[0] += 1 # add 1 to angry count
        
    if (':)' )in str(leitem): # if tweet contains happy but not 'not happy'
        emotion[1] += 1 # add 1 to happy count
        
    if (':(') in str(leitem): # if tweet contains sad
        emotion[2] += 1 # add 1 to sad count

        
        

        
        
