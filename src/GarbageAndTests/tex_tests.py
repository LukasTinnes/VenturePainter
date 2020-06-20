from src.Texture import Texture
from PIL import Image
import numpy

img = Image.open(r"../../Resources/A2.png")
#img = Image.open(r"..\..\Resources\marble.png").convert('L')
tex = Texture(img)
# new_img = tex.stochastic((100,100))
# kernel = numpy.array([[1,2,1],[2,4,2],[1,2,1]])
kernel = numpy.array([[0.5, 1, 2, 1, 0.5], [1, 2, 4, 2, 1], [0.5, 1, 2, 1, 0.5]])
kernel = kernel / numpy.sum(kernel)
# new_img = tex.growing((30,30), kernel, [1,1,20,20], 5)
new_img = tex.quilting((2000, 2000), (20, 20))
# new_img = tex.stochastic((2000,2000))
new_img.show()
