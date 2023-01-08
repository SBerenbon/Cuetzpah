#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pydub import AudioSegment
from pydub.utils import mediainfo
import os, os.path
from benrifunctions import *
from traceback import print_exc

try:
	testSysArgv=sys.argv[1]
except:
	sys.exit()

def refineTime(timeRaw):
	timeRawOriginal=timeRaw
	timeMillis=0
	timeRaw=timeRaw.split(":")
	if len(timeRaw)==3:
		print(timeRaw)
		#minutes and seconds and milliseconds, right?
		timeMillis+=int(timeRaw[2])
		timeMillis+=1000*int(timeRaw[1])
		timeMillis+=60*1000*int(timeRaw[0])
		return timeMillis
	else:
		return -1

def main(audios):
	currentdirectory=sys.path[0]
	for audio in audios:
		try:
			startsAndNames={}
			audio=os.path.abspath(audio)
			bitrate = mediainfo(audio)['bit_rate']
			audioFolder=os.path.split(audio)[0]
			audioBasename=os.path.splitext(os.path.split(audio)[1])[0]
			extension=os.path.splitext(audio)[1].lower()
			extensionDotless=extension.split(".")[1]
			if extensionDotless=="m4a" or extensionDotless=="mp4":
				extensionDotless="ipod"
			cuttingTimes=[]
			cuttingTimesRaw=[]
			endingTimes=[]
			endingTimesRaw=[]
			rawTimes=[]
			rawNames=[]
			cuttingFile=opentoread(audioBasename+".cue")
			tracks=cuttingFile.split("FILE")[1].split("TRACK ")[1:]
			for track in tracks:
				#each INDEX 00 is when a song starts
				trackNumber=track.split(" ")[0]
				performer="Artist"
				title="Title"
				start=None
				endOfLast=None
				if "PERFORMER " in track:
					performer=track.split("PERFORMER ")[1].split("\n")[0][1:-1]
				if "TITLE " in track:
					title=track.split("TITLE")[1].split("\n")[0].strip()[1:-1]
				print(performer+" - "+trackNumber+" - "+title)
				rawNames.append(performer+" - "+trackNumber+" - "+title)
				if "INDEX 00" in track:
					endOfLast=track.split("INDEX 00")[1].split("\n")[0].strip()
					endingTimesRaw.append(endOfLast)
				if "INDEX 01" in track:
					start=track.split("INDEX 01")[1].split("\n")[0].strip()
					cuttingTimesRaw.append(start)
			#if we have INDEX 00, that's when the song starts
			#if we don't, INDEX 01 is when the song starts
			for cuttingTimeRawIndex in range(0, len(cuttingTimesRaw)):
				cuttingTimeRaw=cuttingTimesRaw[cuttingTimeRawIndex]
				endingTimeRaw=None
				if cuttingTimeRawIndex<len(endingTimesRaw):
					endingTimeRaw=endingTimesRaw[cuttingTimeRawIndex]
				refinedTime=refineTime(cuttingTimeRaw)
				if endingTimeRaw:
					refinedBeforeTime=refineTime(endingTimeRaw)
				if refinedTime>-1:
					songName=rawNames.pop(0)
					cuttingTimes.append(refinedTime)
					if endingTimeRaw:
						endingTimes.append(refinedBeforeTime)
					startsAndNames[refinedTime]=filenameFriendly(songName)
					
			masterAudio=AudioSegment.from_file(audio)
			for i in range(0, len(startsAndNames.keys())):
				startTime=cuttingTimes[i]
				endTime=0
				if i<len(endingTimes):
					endTime=endingTimes[i]
				if endTime>0:
					currentTrack=masterAudio[startTime:endTime]
				else:
					currentTrack=masterAudio[startTime:]
				trackFilename=startsAndNames[startTime]+extension
				currentTrack.export(os.path.join(audioFolder, trackFilename), format=extensionDotless, bitrate=bitrate)
		except FileNotFoundError:
			pass
if __name__ == "__main__":
	if len(sys.argv[1:]):
		audios=sys.argv[1:]
	else:
		sys.exit()
	main(audios)
