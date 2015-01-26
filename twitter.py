import time
import csv
import random
from TwitterAPI import TwitterAPI

# [angry, happy, sad]
emotion = [0,0,0]

# [R,G,B]
colour = [0,0,0]

# number of times colour has been logged
count = 0

# delay between each log
delay = 10

# sets timer
timeout = time.time() + delay

# Twitter API setup
TRACK_TERM = 'angry, annoyed, happy, sad, upset'

# KEEP SECRET
CONSUMER_KEY = 'ecScSfb0Y7R2rbLiWZG5P8p9D'
CONSUMER_SECRET = 'XCWKU7gRMlnhZHW04pD3P8BCtYO2PB75103ydFVyTJK8xmabEx'
ACCESS_TOKEN_KEY = '2268616653-KQOSziHX2psAxf6upZXokQdmOFpFr6GCnGuQK7c'
ACCESS_TOKEN_SECRET = '3ZF1KUnYlL96UPJWxMnA8oRJw1Cr4aLAqSnAZE46id4kc'

api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)


# Determines R, G, B outputs 
def whatColour():
    global colour
    totalNum = sum(emotion) # number of tweets analysed
    largestNum = max(emotion) # mode emotion
    intensity = (largestNum / totalNum) * 255 # mode emotion / number of tweets * 255(Maximum RGB value)
    intensity = round(intensity, 2) # Rounds intensity to 2 d.p
    selectedColour = emotion.index(largestNum) # Works out which emotion appears most often
    colour[selectedColour] = intensity # Sets the corresponding light.
    print("colour", colour)# Prints the output for debugging


#MAIN PROGRAM
with open('output.csv', 'w', newline='') as csvfile: # opens CSV file
    wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) # opens a wrtie command for CSV file

    # Twitter API call
    r = api.request('statuses/filter', {'track': TRACK_TERM})

    for item in r: # for each tweet
        if time.time() > timeout: # If time elapsed
            print('emotion', emotion)
            whatColour() # Determines R, G, B outputs 
            wr.writerow(colour) #writes the RGB colour to the csv
            colour = [0,0,0] # resets colour
            emotion = [0,0,0] # resets tweet count
            time.sleep(2) # 2 second delay...
            timeout = time.time() + delay #resets timer
            count += 1 # adds 1 to the count of rows added
        
        #Manipulates tweet to add to emotion counter    
        leitem = item['text'] if 'text' in item else item # select tweet text
        leitem = leitem.encode('utf-8') # encode it so python reconises it
        if ('angry' or 'annoyed') in str(leitem): # if tweet contains angry
            emotion[0] += 1 # add 1 to angry count
            
        if 'happy' in str(leitem): # if tweet contains happy but not 'not happy'
            emotion[1] += 1 # add 1 to happy count
            
        if ('sad' or 'upset') in str(leitem): # if tweet contains sad
            emotion[2] += 1 # add 1 to sad count

        
        

        
        
