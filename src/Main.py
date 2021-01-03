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
    cv2.imshow("Title", Texture.condiments([500,500],[np.array([1,0,0]),np.array([0,1,0]), np.array([0,0,1])]))
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
