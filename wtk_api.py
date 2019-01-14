'''
Created by PARANGAT BHASKAR on 1/13/19.
Copyright © 2019 PARANGAT. All rights reserved.

BEFORE YOU GET STARTED:
1. Get you unique API key (check lines 20-24)
2. Update the email on line (check line 47)
3. Reach out to me on Linkedin (Parangat Bhaskar) for any further questions.
'''

#import library to request data from NREL server:
import urllib.request, urllib.parse, urllib.error
import sys

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#DEFINE PARAMETERS:
#Alter any or all of these parameters as per your requirement.

#--------------------------------------------------------------------------------------------------------------------------------------------#
#You will need an API key to get access to this data. Consider this your ID card if you like.
#Get your unique API key here: https://developer.nrel.gov/signup/
#Replace your api key with the dummy api below:

api_key = 'adjbcWIUHBijbndscjkn'    #Note: This is a dummy api key! You will need to request your own API key.

#--------------------------------------------------------------------------------------------------------------------------------------------#

#Well Known Text point string. This is the syntax for representing a point (or coordinate) in the US.

wkt = 'POINT(-77.8600 40.7934)'     #Syntax: 'POINT(longitude latitude)'
                                    #Note: Longitudes west of the Greenwich meridean are negative.
#--------------------------------------------------------------------------------------------------------------------------------------------#

#Each specified attribute will be returned as a column in the resultant CSV download.
#Attributes include: [wind_speed, wind_direction, power, pressure, temperature, density]

attributes = '[wind_speed, wind_direction, power, pressure, temperature, density]'
#--------------------------------------------------------------------------------------------------------------------------------------------#

#Input years you want data for (limited to 2007-2013).
names = '2012'

#--------------------------------------------------------------------------------------------------------------------------------------------#

#An active email for the user requesting data. This email will be used to deliver the extracted data.

email = 'dummy_messenger@dummymail.com' #Add your email. This is required.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


filename = input('Choose a name for your file: (Include .txt extension at the end. Example: wind_data_2012.txt)     ')
while True:
    if filename == 'EXIT':
        sys.exit('==== QUITTING ====')
    elif '.txt' not in filename:
        filename = input('Invalid filename syntax. Please include the .txt extension! Try again (Type EXIT to quit)     ')
    else: break

#Website URL: (Entry point to the API)
#Do not change any of the following code!
serviceurl = 'https://developer.nrel.gov/api/wind-toolkit/wind/wtk_download.csv?'
url = serviceurl + urllib.parse.urlencode({'api_key': api_key , 'wkt':wkt, 'attributes':attributes, 'names':names,'email':email})
print(url)
print ('Retrieving', url)

#Connect to port 80 of server and send a GET request to obtain data:
uh = urllib.request.urlopen(url)

#Read data being sent by server:
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

#Write data to a TEXT file in your computer. This contains comma delimited data which can directly be opened in Microsoft Excel as a CSV file
#Note: Find your current working directory (cwd). Your cwd is where this file is created.
fhandle = open(filename, 'w+')
for line in data:
    fhandle.write(line)
