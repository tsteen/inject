#!/usr/bin/python
import json, dicttoxml, os, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-xml.py /path/to/file.json')
fileIn = sys.argv[1]
fileOnly = os.path.basename(fileIn)
try:
	fileOut = sys.argv[2]
except:
	fileList = [fileOnly.split('.')[0], 'xml']
	fileOut = ".".join(fileList)

# read the json file filename in
input = open(fileIn)
data = json.load(input)
input.close()

# convert to xml
xml = dicttoxml.dicttoxml(data)

# write the xml file
with open(fileOut, "wb+") as outfile:
	outfile.write(xml)
