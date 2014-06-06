from kivy.app import App
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
Builder.load_string('''
[Title@Label]
    pos_hint: {'center_x': .5, 'y': .3}
    text: ctx.text
    font_size: 16
<RotationWid>:
    FloatLayout:
        Title:
            text: root.message
        Image:
            source: 'kivy.png'
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.angle
                    origin: self.center
            canvas.after:
                PopMatrix
        Image:
            source: 'Red.png'
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.angle
                    origin: self.center
            canvas.after:
                PopMatrix
        Image:
            source: 'tinyCompass.png'
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.angle
                    origin: self.center
            canvas.after:
                PopMatrix
''')
class RotationWid(FloatLayout):
    angle = NumericProperty(-45)
    message = '45 degrees'
   
class RotationApp(App):
    def build(self):
        return RotationWid()
RotationApp().run()