import utils, sys, time

# import Clever Library
import clever

# import icecast stats library
import stats

# import tendo singleton class
import singleton

# create single instance lock
instance = singleton.SingleInstance()

# debug flags
debuging = False

# create log objects
buffer_log = utils.log('buffer_log.txt')
connect_log = utils.log('connect_log.txt')

# path to the settings file
settingsFile = "settings.xml"
# create a settings object
config = utils.settings(settingsFile)

# --- Load Settings --- #
# Rate for reads in milliseconds
rate = int(config.getSetting("rate"))
ratePS = 1000 / rate

# allowable offset of equivilent time values in milliseconds
offset = int(config.getSetting("offset")) / 1000.0

# range of skip monitor in decimal
skipRange = int(config.getSetting("range")) / 1000.0

# max skips in range before restart
skipLimit = int(config.getSetting("skip-limit"))

# resets before fallback
resets = int(config.getSetting("resets"))
resetsUsed = 0

# fallback file
fallback = config.getSetting("fallback")

# icecast server URL
serverUrl = config.getSetting("server-url")

# store last client connect time
clientConnect = stats.streamTime(serverUrl)
connect_log.log("Client Connect*: " + str(clientConnect))

# set time to stop monitoring stream
# get from arg if available
if (len(sys.argv) > 1): stopTime = sys.argv[1]
# else set to an unreachable time value
else: stopTime = "25:60"

# list of stream position readings and skips
reads = []
skips = []

# catch exceptions
try:
	# loop till stop time
	while not utils.past(stopTime):
		# read server stats
		statRead = stats.streamTime(serverUrl)
		if statRead != clientConnect:
		    clientConnect = statRead
		    connect_log.log("Client Reconnect: " + str(clientConnect))
		# read position in stream
		reads.append([clever.position(), time.time()])
		print ""
		l = len(reads)
		# begin monitoring once 1 second has occured
		if l > ratePS:
			readDiff = (reads[l-1][0] - reads[l-(ratePS + 1)][0]) / 1000.0
			clockDiff = reads[l-1][1] - reads[l-(ratePS + 1)][1]
			skip = abs(readDiff - clockDiff) > offset
			if debuging: print readDiff - clockDiff, skip

			if skip:
				skips.append(reads[l-(ratePS + 1)])
				if debuging: print "# of Skips: ", len(skips)

				# if skip limit is reached in range, try reset
				if (len(skips) > skipLimit) and (time.time() - skips[-skipLimit][1]) <= skipRange:
					buffer_log.log("Stream Restart")
					if resetsUsed < resets:
						clever.stop()
						clever.play()
						skips = []
						resetsUsed += 1
						while (clever.position() == 0):
							pass
						time.sleep(skipRange)
					else:
						clever.loadplay(fallback)
						raise Exception("buffer fallback")
				else:
					buffer_log.log("Stream Buffer")

        # delay before next read
		time.sleep(rate/1000.0)

except KeyboardInterrupt:
	print "Buffer Monitor Exiting"

except Exception, Argument:
	print "Exception Raised at Runtime:", Argument
