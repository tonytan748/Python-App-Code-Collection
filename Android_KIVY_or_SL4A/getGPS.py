# -*- coding: utf-8 -*-
import android
import time
from math import radians
droid = android.Android()
droid.startSensingTimed(1, 250)
droid.startLocating()
while 1:
    gpsdata = droid.readLocation().result
    s6data = droid.sensorsReadOrientation().result
    if len(gpsdata)>0:
        print gpsdata['gps']['bearing'] #取得Gps导向(bearing)(角度)
    if len(s6data)>0:
        print s6data[0] #取得罗盘方位角(azimuth)(弧度)
    time.sleep(0.5)
droid.stopLocating()
droid.stopSensing()