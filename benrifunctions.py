#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import strftime
import os, os.path
strftimeformat=strftime("%Y-%m-%d_%H-%M-%S")

def removekey(d, key):
	r = dict(d)
	del r[key]
	return r

def splitOnJustFirstInstance(theString, theToken):
	return theString.split(theString.split(theToken)[0]+theToken)[1]

def splitOnJustLastInstance(theString, theToken):
	return theString.split(theToken+theString.split(theToken)[-1])[0]

def nesteddictprint(thedict):
	finalstring="{"
	for i in sorted(thedict.keys()):
		finalstring+="'"+i+"':{"
		for j in sorted(thedict[i].keys()):
			finalstring+="'"+j+"':"+repr(thedict[i][j])+",\n"
		finalstring+="},\n"
	finalstring+="}"
	return finalstring

def dictprint(thedict):
	finalstring="{"
	for i in sorted(thedict.keys()):
		finalstring+=repr(i)+":"+repr(thedict[i])+",\n"
	finalstring+="}"
	return finalstring

#a=dictprint({"a":1,"b":2})
#print(a)

def opentoread(nameoffile):
	f=open(nameoffile, "r")
	ff=f.read().replace("\r\n", "\n").replace("\r", "\n")
	f.close()
	return ff

def opentoreadbinary(nameoffile):
	f=open(nameoffile, "rb")
	ff=f.read()
	f.close()
	return ff

def writethistothis(contents, nameoffile):
	fil=open(nameoffile, "w")
	fil.write(contents)
	fil.close()

def writethistothisbinary(contents, nameoffile):
	fil=open(nameoffile, "wb")
	fil.write(contents)
	fil.close()

def multiline_input(prompt):
	text=""
	print(prompt)
	while True:
		try:
			text+=input(">>>")+"\n"
		except KeyboardInterrupt:
			print()
			break
	return text.strip()

def saveFileTimeData(filepath):
	thefile=os.path.abspath(filepath)
	modifiedTime=os.path.getmtime(thefile)
	accessedTime=os.path.getatime(thefile)
	timeData=[modifiedTime, accessedTime]
	return timeData

def restoreFileTimeData(filepath, accessedTime, modifiedTime):
	os.utime(filepath, (accessedTime, modifiedTime))

def filenameFriendly(string):
	return string.replace("/","--").replace("\\","-").replace(":","-").replace("\"","").replace("?","")

def xmlify(text):
	return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;").replace("\"", "&quot;")

def pickOne(choices, prompt):
	noInput=True
	chosenOne=None
	while noInput:
		counter=1
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		pick=input(prompt+"\n>>>")
		try:
			chosenOne=choices[int(pick)-1]
			noInput=False
		except:
			print("Invalid input.")
	return chosenOne
	
def pickOneIndex(choices, prompt):
	noInput=True
	pick=-1
	while noInput:
		counter=1		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		pick=input(prompt+"\n>>>")
		try:
			pick=int(pick)-1
			if pick<0 or pick>=len(choices):
				raise Exception
			else:
				noInput=False
		except:
			print("Invalid input.")
	return pick
	
def pickMany(choices, prompt):
	noInput=True
	while noInput:
		counter=1
		thePicked=[]		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		picks=input(prompt+" (1,2,3...)\n>>>")
		if "," in picks:
			picks=picks.split(",")
		else:
			picks=[picks]
		try:
			for pick in picks:
				if choices[int(pick)-1] not in thePicked:
					thePicked.append(choices[int(pick)-1])
			if len(thePicked):
				noInput=False
		except:
			print("Invalid input.")
	return thePicked

def pickManyIndexes(choices, prompt):
	noInput=True
	while noInput:
		thePicked=[]
		counter=1		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		picks=input(prompt+" (1,2,3...)\n>>>")
		if "," in picks:
			picks=picks.split(",")
		else:
			picks=[picks]
		try:
			for pick in picks:
				if int(pick)-1 not in thePicked:
					thePicked.append(int(pick)-1)
			if len(thePicked):
				noInput=False
		except:
			print("Invalid input.")
	return list(reversed(sorted(thePicked)))
def pickOneOrCancel(choices, prompt):
	noInput=True
	chosenOne=None
	while noInput:
		counter=1		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		print(str(counter)+" Cancel")
		pick=input(prompt+"\n>>>")
		if pick==str(counter):
			noInput=False
		else:
			try:
				print(pick)
				pick=int(pick)-1
				print(choices)
				chosenOne=choices[pick]
				
				print(chosenOne)
				noInput=False
			except:
				print("Invalid input.")
	return chosenOne
	
def pickOneIndexOrCancel(choices, prompt):
	noInput=True
	pick=-1
	while noInput:
		counter=1
		pick=-1		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		print(str(counter)+" Cancel")
		pick=input(prompt+"\n>>>")
		if pick==str(counter):
			noInput=False
		else:
			try:
				pick=int(pick)-1
				if pick<0 or pick>=len(choices):
					raise Exception
				else:
					noInput=False
			except:
				print("Invalid input.")
	return pick
	
def pickManyOrCancel(choices, prompt):
	noInput=True
	thePicked=[]
	while noInput:
		counter=1
		thePicked=[]		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		print(str(counter)+" Cancel")
		picks=input(prompt+" (1,2,3...)\n>>>")
		if picks==str(counter):
			noInput=False
		elif "," in picks:
			picks=picks.split(",")
			if str(counter) in picks:
				noInput=False
		else:
			picks=[picks]
		try:
			for pick in picks:
				if choices[int(pick)-1] not in thePicked:
					thePicked.append(choices[int(pick)-1])
			if len(thePicked):
				noInput=False
		except:
			print("Invalid input.")
	return thePicked

def pickManyIndexesOrCancel(choices, prompt):
	noInput=True
	thePicked=[]
	while noInput:
		counter=1
		thePicked=[]		
		for i in choices:
			print(str(counter)+" "+str(i))
			counter+=1
		print(str(counter)+" Cancel")
		picks=input(prompt+" (1,2,3...)\n>>>")
		if picks==str(counter):
			noInput=False
		elif "," in picks:
			picks=picks.split(",")
			if str(counter) in picks:
				noInput=False
		else:
			picks=[picks]
		try:
			for pick in picks:
				if int(pick)-1 not in thePicked:
					thePicked.append(int(pick)-1)
			if len(thePicked):
				noInput=False
		except:
			print("Invalid input.")
	return list(reversed(sorted(thePicked)))

def commaJoinList(theList):
	for i in range(0, len(theList)):
		if type(theList[i])!=str:
			theList[i]=str(theList[i])
	return ", ".join(theList)

def semicolonJoinList(theList):
	for i in range(0, len(theList)):
		if type(theList[i])!=str:
			theList[i]=str(theList[i])
	return "; ".join(theList)

def listToStringSemicolon(theList):
	if type(theList)==list:
		if len(theList)==1:
			if type(theList[0])==str:
				return theList[0]
			else:
				return str(theList[0])
		elif len(theList)>1:
			return semicolonJoinList(theList)
		else:
			return ""
	else:
		return str(theList)

def listToStringComma(theList):
	if type(theList)==list:
		if len(theList)==1:
			if type(theList[0])==str:
				return theList[0]
			else:
				return str(theList[0])
		elif len(theList)>1:
			return commaJoinList(theList)
		else:
			return ""
	else:
		return str(theList)

def makeUniqueFilename():
	return "file"+strftime("%Y-%m-%d %H-%M-%S")
