from src.Texture import Texture
from PIL import Image

img = Image.open(r"..\..\Resources\marble.png")
tex = Texture(img)
new_img = tex.growing((100,100), [], [10,10,20,20])
new_img.show()
