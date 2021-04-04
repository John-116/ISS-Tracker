# ISS TRACKER
I made this tracker using the ephem module in python.

It uses TLE data from NORAD to get the co-ordinates of the ISS

#### Modules I used
I used 3 modules in the python code
    1. Ephem - for the Maths functions in TLE
    2. Requests - to get tle from the URLs
    3. Pyperclip - to add things to clipboard

I added an exe which is independent of python I used the pyinstaller module to create it
###### Use this command as pyinstaller
pyinstaller --onefile --icon=ISS_Tracker.ico ISS_Tracker.py

