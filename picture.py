"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, .7)
green = Color(0x00ff00, .7)
blue = Color(0x0000ff, .7)
black = Color(0x000000, .7)


thinline = LineStyle(1, black)
rect = RectangleAsset(400,5, thinline, black)
Sprite(rect, (20,40))

thinline = LineStyle(1, black)
rect = RectangleAsset(400,5, thinline, black)
Sprite(rect, (20,300))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
