from src.Texture import Texture
from PIL import Image
import numpy

img = Image.open(r"..\..\Resources\marble.png")
tex = Texture(img)
new_img = tex.growing((100,100), 1/16 * numpy.array([[1,2,1],[2,4,2],[1,2,1]]), [1,1,2,2], 1)
new_img.show()
