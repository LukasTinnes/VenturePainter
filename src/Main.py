import logging
import os
from tkinter import *
from tkinter import filedialog

from src.Loader import Loader

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                               filetypes=[("SVG-Image", "*.svg"), ("png image", "*.png"),
                                                          ("jpg image", "*.jpg *.jpeg"),
                                                          ("tagged image file", "*.tiff *.tif"), ("All files", "*.*")])
    folder_path = os.path.dirname(root.filename)
    logging.basicConfig(filename='example.log', level=logging.INFO)
    loader = Loader(folder_path)
    background = loader.load(root.filename)
    print(background)
    # interpreter = Interpreter()
    # hierarchy = interpreter.interpret(background, shapes)
    # painter = Painter()
    # img = painter.paint(hierarchy, background, shapes, camera)
    # img.show()
