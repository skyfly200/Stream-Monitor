import os.path, re, time, random
import xml.etree.ElementTree as xmlProcessor

# class for manipulating the log file
class log(object):
	# open or create log file
	def __init__(self, path="log.txt", name="Log File"):
		self.logPath = path
		self.logName = name
		# check if file exists
		exists = os.path.isfile(self.logPath)
		# if log file dosn't exist, then create it and write the header line
		if not exists:
			with open(self.logPath, 'a') as f:
				f.write("---" + self.logName + " Log File---\n")

	# log any value to the log file
	def log(self, log):
		with open(self.logPath, 'a') as f:
			f.write(time.strftime('%c') + " :\n" + str(log) + "\n")

	# return the last log in the log file
	def lastLog(self):
		log = False
		with open(self.logPath) as f:
			log = f.readlines()[-1]
		return log

	# return the timestamp of the last log in the log file
	def lastLogTime(self):
		timestamp = False
		with open(self.logPath) as f:
			timestamp = f.readlines()[-2][:-3]
		return timestamp

# settings object
class settings():
	# instantiate a settings object
	def __init__(self, xmlFile):
		# parse the xml file
		self.root = self.parseXML(xmlFile)

	# process the xml file object
	def parseXML(self, xmlFile):
		settingsFile = xmlProcessor.parse(xmlFile)
		return settingsFile.getroot()

	# get a setting tags value
	def getSetting(self, name):
		return self.root.find(name).text

	# get a setting tags attribute
	def getSettingAttr(self, name, attr):
		return self.root.find(name).get(attr)


def past(t):
	tParts = t.split(":")
	return int(tParts[0]) < int(time.strftime("%H")) or int(tParts[0]) == int(time.strftime("%H")) and int(tParts[1]) < int(time.strftime("%M"))
