# Stream-Monitor
Monitors streams for buffering, reset and/or fallback
Works with winamp playing streams

Requires Python 2.7 and PIP

## Using the Script
Download the zip  file and extract the contents.

Open a terminal in the Stream-Monitor folder

Run depend.bat to install the following dependencies (windows only)<br>
<b><i>requests, pytz, iso8601</i></b><br>
otherwise install them using PIP

Run the script in the terminal like so<br>
<b><i>python BuffMon.py</i></b>

Optionaly run the script with a timeout in 24 hour time like so<br>
<b><i>python BuffMon.py 14:30</i></b><br>
(stop monitoring the stream at 2:30 PM)

Script resets stream untill resets are exhausted.
It then loads the fallback file

Number of resets, fallback file, monitor range, skip limit, read rate and offset threshold sare user setable options.

The script will read options from settings.xml
more info on option can be found there
