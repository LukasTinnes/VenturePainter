from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter
import logging
import datetime
import os
from tkinter import *
from tkinter import filedialog
import cv2


if __name__ == "__main__":
    from src.Texture import Texture
    import numpy as np
    #img = Texture.simplexNoise([500,500], scale_x=50, scale_y=50)
    img = Texture.sine_perlin([500,500], sine_scale=0.1, perlin_scale=20, randomness=20)

    cv2.imshow("Title", img)
    cv2.waitKey(0)
    logging.basicConfig(filename='log.log', level=logging.INFO)
    logging.info(f"started execution at {datetime.datetime.now()}")
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                               filetypes=[("SVG-Image", "*.svg"), ("png image", "*.png"),
                                                          ("jpg image", "*.jpg *.jpeg"),
                                                          ("tagged image file", "*.tiff *.tif"), ("All files", "*.*")])
    folder_path = os.path.dirname(root.filename)
    loader = Loader()
    shapes = loader.load(root.filename)
    interpreter = Interpreter()
    hierarchy = interpreter.interpret(shapes)

    #painter = Painter()
    #img = painter.paint(hierarchy, background, shapes, camera)
    #img.show()
