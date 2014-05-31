#-*-coding=utf-8-*-

import os
import sys

radio_list={'MPR News':'mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/news.pls',
'The Current':'mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/the_current.pls',
'Classical MPR':'mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/classical.pls',
'Local Current':'mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/local.pls',
'MPR Radio Heartland':'mplayer -playlist http://minnesota.publicradio.org/tools/play/streams/radio_heartland.pls',
'MPR Wonderground Windows Media':'mplayer http://wondergroundstream2.publicradio.org/wonderground',
'Clasical MPR Choral':'mplayer -playlist http://choralstream1.publicradio.org/choral.m3u',
'WEFUNK Radio MP3 64K':'mplayer -playlist http://www.wefunkradio.com/play/shoutcast.pls',
'Sleepbot Environmental Broadcast 56K MP3':'mplayer -playlist http://sleepbot.com/ambience/cgi/listen.cgi/listen.pls',
'Soma FM Groove Salad iTunes AAC 128K':'mplayer -playlist http://somafm.com/groovesalad130.pls',
'Soma FM Drone Zone iTunes AAC 128K':'mplayer -playlist http://somafm.com/dronezone130.pls',
'Soma FM Lush iTunes AAC 128K':'mplayer -playlist http://somafm.com/lush130.pls',
'Soma FM Sonic Universe iTunes AAC 128K':'mplayer -playlist http://somafm.com/sonicuniverse.pls'
}

x={}
for i,item in enumerate(radio_list.keys()):
	x[i]=item
	print '%d -- %s' % (i,item)

isSelect=False
while isSelect==False:
	a=raw_input('Please select which radio you want listen?')
	if a:
		print a
		if int(a) in range(len(x)):
			items=x[int(a)]
			select_radio=radio_list[items]
			print select_radio
			os.system(select_radio)
			isSelect=True
		elif a.upper() == 'EXIT':
			sys.exit(0)

