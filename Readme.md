# ISS TRACKER
I made this tracker using the ephem module in python.

It uses TLE data from NORAD to get the co-ordinates of the ISS

## Modules I used
I used 3 modules in the python code
- Ephem
- Requests
- Pyperclip

## Making an executable via pyinstaller
I made an executable that is independent of python if you want to try it out without downloading any of the packages
To make this executable I used pyinstaller
I inserted this command which tells pyinstaller 3 things
1. Make the executable one file
2. Define the icon
3. Define the target file
pyinstaller --onefile --icon=ISS_Tracker.ico ISS_Tracker.py

###### Ensure that when you install pyinstaller you install in a command prompt that is run as admin otherwise pyinstaller won't be added to path and you won't be able to call on pyinstaller

Thank you and stay safe, John

