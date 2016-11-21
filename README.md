# Stream-Monitor
Monitors streams for buffering, reset and/or fallback
Works with winamp playing streams

Requires Python 2.7

## Using the Script
Download the zip  file and extract the contents.

Open a terminal in the Stream-Monitor folder

Run the script in the terminal like so
<i>python BuffMon.py</i>

Optionaly run the script with a timeout in 24 hour time like so
<i>python BuffMon.py 14:30</i>
(stop monitoring the stream at 2:30 PM)

Script resets stream untill resets are exhausted.
It then loads the fallback file

Number of resets, fallback file, monitor range, skip limit, read rate and offset threshold sare user setable options.

The script will read options from settings.xml
more info on option can be found there
