# SatTrack 
I made this Satellite tracker using the ephem module in python.

It uses TLE data from NORAD (https://celestrak.com/NORAD/elements/stations.txt) to get the co-ordinates of satellites


## Modules I used
You can download them with 
pip install -r r.txt
I used 3 modules in the python code
- Ephem
- Requests
- Pyperclip

## Making an executable via pyinstaller
If you want to make an executable out of this file use pyinstaller (command below).
I had an exe on this repo but took it down as my anti-virus was flagging it as a Trojan
I inserted this command which tells pyinstaller 3 things
1. Make the executable one file
2. Defines the icon file
3. Define the target python file to turn into an executable
    pyinstaller --onefile --icon=ISS_Tracker.ico ISS_Tracker.py

###### Ensure that when you install pyinstaller you install in a command prompt that is run as admin otherwise pyinstaller won't be added to path and you won't be able to call on pyinstaller

Thank you and stay safe, John

