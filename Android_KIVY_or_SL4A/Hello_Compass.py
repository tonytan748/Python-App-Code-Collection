#qpy:webapp:Hello Compass
#qpy://localhost:8080/     #这个注释行是必要的指令
"""
This is a sample for qpython webapp
"""
from bottle import route, run
import androidhelper
import time
code = '''
<html>
<body>
<center>
<canvas id="myCanvas" width="300" height="300" style="border:1px solid #d3d3d3;">
</canvas>
<button onclick="int=window.clearInterval(int);stopCompass()">
shut down</button>
</center>
<script language=javascript>
var az;
var deg;
var canv =document.getElementById("myCanvas");
var ctx =canv.getContext("2d");
var cx = canv.width /2;
var cy = canv.height /2;
function drawCompass()
{
ctx.clearRect(0, 0, canv.width, canv.height);
ctx.strokeStyle = "black";
ctx.lineWidth = 3
ctx.font = "12pt";
ctx.textAlign="left";
ctx.fillText(deg,5,15);
ctx.fillText("N", cx-5, cy-105);
ctx.fillText("S", cx-5, cy+115);
ctx.fillText("W", cx-115, cy+5);
ctx.fillText("E", cx+105, cy+5);
ctx.beginPath();
ctx.arc(cx,cy,100,0,2*Math.PI);
ctx.arc(cx,cy,100,0,az);
ctx.lineTo(cx,cy);
ctx.stroke();
}
var int=self.setInterval("clock()",500);
function clock()
{
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://localhost:8080/azimuth", false);
xhr.send(null);
az=parseFloat(xhr.responseText);
if(az>=0){
deg = String(az*180/Math.PI);
}else{
deg = String(360+az*180/Math.PI);
}
az=az-(0.5*Math.PI);
drawCompass();
}
function stopCompass()
{
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://localhost:8080/stopCompass", false);
xhr.send(null);
t=xhr.responseText;
document.getElementById("req").value=t;
}
</script>
</body>
</html>
'''
droid = androidhelper.Android()
droid.startSensingTimed(1, 250)
@route('/')
def index():
    return code
@route('/azimuth')
def azimuth():
    s6data = droid.sensorsReadOrientation().result
    if len(s6data)>0:
        return str(s6data[0])
@route('/stopCompass')
def stopCompass():
    droid.stopSensing()
    return str(1)
run(host='localhost', port=8080)
droid.stopSensing()