# ISS Tracker 03/04/2021
from ephem import readtle, degree 
import requests
import pyperclip

# Gathers 2 Line Element Data from NORAD
website = requests.get(url="https://celestrak.com/NORAD/elements/stations.txt")
lines = website.text.split("\n")
Title = lines[0]
LineI = lines[1]
LineII = lines[2]
ISStle = readtle(Title, LineI, LineII)

ISStle.compute() # Calculate's location in Degrees Minute Seconds

latitude = ISStle.sublat/degree # Converts from DMS to latitude
longitude = ISStle.sublong/degree # Converts from DMS to longitude
mapurl = "https://www.openstreetmap.org/#map=6/"+ str(latitude) + "/" + str(longitude) # Creates the openstreetmap url

print("""

 ▄█     ▄████████    ▄████████          ███        ▄████████    ▄████████  ▄████████    ▄█   ▄█▄ 
███    ███    ███   ███    ███      ▀█████████▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀ 
███▌   ███    █▀    ███    █▀          ▀███▀▀██   ███    ███   ███    ███ ███    █▀    ███▐██▀   
███▌   ███          ███                 ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀    
███▌ ▀███████████ ▀███████████          ███     ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    
███           ███          ███          ███     ▀███████████   ███    ███ ███    █▄    ███▐██▄   
███     ▄█    ███    ▄█    ███          ███       ███    ███   ███    ███ ███    ███   ███ ▀███▄ 
█▀    ▄████████▀   ▄████████▀          ▄████▀     ███    ███   ███    █▀  ████████▀    ███   ▀█▀ 
                                                  ███    ███                           ▀         

                                                                      """) # Title line

print("ISS's current latitude:  " + str(latitude))
print("ISS's current longitude: " + str(longitude) + "\n")


print("The location's url has been copied to your clipboard")
print(mapurl + "\n")
pyperclip.copy(mapurl) # Copies the url to Clipboard
print("Any Issues please contact me on GitHub @John-116")
keepappopen = input("Thank You For using ISSTrack!") # Asks for input to stop the program from terminating when in an exe



    

