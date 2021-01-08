import datetime
import logging
import os
from tkinter import *
from tkinter import filedialog

import pygame
import json
from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter
from src.SurfaceInfos.SurfaceInfoNoContext import SurfaceInfoNoContext

if __name__ == "__main__":
    logging.basicConfig(filename='log.log', level=logging.INFO)
    logging.info(f"started execution at {datetime.datetime.now()}")

    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                               filetypes=[("SVG-Image", "*.svg"), ("png image", "*.png"),
                                                          ("jpg image", "*.jpg *.jpeg"),
                                                          ("tagged image file", "*.tiff *.tif"), ("All files", "*.*")])
    folder_path = os.path.dirname(root.filename)
    logging.info(f"Acquired file name")


    with open("info.json") as file:
        js = json.load(file)
    action_dict = {key: SurfaceInfoNoContext.from_json(js[key]) for key in js.keys()}
    logging.info("Loaded action dict")

    loader = Loader()
    shapes = loader.load(root.filename)
    interpreter = Interpreter()
    hierarchy = interpreter.interpret(shapes)
    painter = Painter()
    viewing_window = pygame.Rect(0, 0, 500, 500)
    img = painter.paint(hierarchy, shapes, viewing_window, action_dict)
