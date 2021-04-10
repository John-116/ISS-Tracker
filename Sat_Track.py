#Sat Track
from ephem import readtle, degree 
import requests
import pyperclip
import os

website = requests.get(url="https://celestrak.com/NORAD/elements/stations.txt")
lines = website.text.split("\n")



print("""
  ▄████████    ▄████████     ███         ███        ▄████████    ▄████████  ▄████████    ▄█   ▄█▄ 
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀ 
  ███    █▀    ███    ███    ▀███▀▀██    ▀███▀▀██   ███    ███   ███    ███ ███    █▀    ███▐██▀   
  ███          ███    ███     ███   ▀     ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀    
▀███████████ ▀███████████     ███         ███     ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    
         ███   ███    ███     ███         ███     ▀███████████   ███    ███ ███    █▄    ███▐██▄   
   ▄█    ███   ███    ███     ███         ███       ███    ███   ███    ███ ███    ███   ███ ▀███▄ 
 ▄████████▀    ███    █▀     ▄████▀      ▄████▀     ███    ███   ███    █▀  ████████▀    ███   ▀█▀ 
                                                    ███    ███                           ▀         
                                                    """)
print("Welcome to Sattrack!")
GetStarted = input("Press enter to Start")


#List of Satellites
print(""" 
[1] ISS (ZARYA)             
[2] KESTREL EYE IIM (KE2M)  
[3] DELLINGR (RBLE)         
[4] TEMPEST-D               
[5] RADSAT-G                
[6] AEROCUBE 12A            
[7] AEROCUBE 12B            
[8] LEMUR-2-VU              
[9] LEMUR-2-ALEXANDER       
[10] LEMUR-2-YUASA           
[11] LEMUR-2-TOMHENDERSON    
[12] 1998-067PN              
[13] STARS-ME                
[14] ISS DEB (SEDA-AP)       
[15] CATSAT-2                
[16] UNITE                   
[17] CATSAT-1                
[18] ISS DEB                 
[19] ISS DEB                 
[20] RAAVANA-1               
[21] UGUISU                  
[22] NEPALISAT-1             
[23] SPOOQY-1                
[24] RED-EYE 1 (PINOT)       
[25] IOD-1 GEMS              
[26] KRAKSAT                 
[27] VCC A                   
[28] ENTRYSAT                
[29] VCC C                   
[30] VCC B                   
[31] ISS DEB                 
[32] ISS DEB                 
[33] RWASAT-1                
[34] AQT-D                   
[35] NARSSCUBE-1             
[36] STPSAT-4                
[37] HARP                    
[38] 1998-067RA              
[39] PHOENIX                 
[40] 1998-067RC              
[41] CRYOCUBE                
[42] AZTECHSAT-1             
[43] RADSAT-U                
[44] QARMAN                  
[45] SORTIE                  
[46] ICS-EF (ISS DEB)        
[47] PROGRESS-MS 14          
[48] G-SAT                   
[49] QUETZAL-1               
[50] RED-EYE 2 (MERLOT)      
[51] RED-EYE 3 (CABERNET)    
[52] DEMI                    
[53] SOYUZ-MS 17             
[54] CREW DRAGON 1           
[55] SPOC                    
[56] BOBCAT-1                
[57] NEUTRON-1               
[58] 1998-067RU              
[59] LEMUR-2-BAXTER-OLIVER   
[60] LEMUR-2-DJARA           
[61] DESCENT                 
[62] PROGRESS-MS 16          
[63] CYGNUS NG-15            
[64] ISS DEB                 
[65] RSP-01                  
[66] TAUSAT-1                
[67] TSURU                   
[68] STARS-EC                
[69] MMSATS-1
""")
Satellite = input("Please enter the number (0-69) of the satellite you would like to track? ")



# Sattelite logic
SatelliteTitle = (int(Satellite) * 3) - 3
SatelliteLineI = (int(Satellite) * 3) - 2
SatelliteLineII = (int(Satellite) * 3) - 1

Title = lines[SatelliteTitle]
LineI = lines[SatelliteLineI]
LineII = lines[SatelliteLineII]
TLE = readtle(Title, LineI, LineII)
TLE.compute()

latitude = TLE.sublat/degree # Converts from DMS to latitude
longitude = TLE.sublong/degree # Converts from DMS to longitude
mapurl = "https://www.openstreetmap.org/#map=6/"+ str(latitude) + "/" + str(longitude) # Creates the openstreetmap url

print("\n")
print("The Satellites current latitude  is  " + str(latitude))
print("The Satellites current longitude is " + str(longitude) + "\n")
print("The location's url has been copied to your clipboard")
print(mapurl + "\n")
pyperclip.copy(mapurl) # Copies the url to Clipboard
print("Thank You For using SatTrack!")
keepappopen = input("Any Issues please contact me on GitHub @John-116")