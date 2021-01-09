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
#from src.Themes.UniformTheme import UniformTheme as Theme
from src.Themes.NeighborTheme import NeighborTheme as Theme
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from matplotlib import gridspec


class Interface:

    def __init__(self):
        # GUI Elements

        self.fig = plt.figure()
        self.gridspec = gridspec.GridSpec(1,2, width_ratios=[0.9,0.1])

        self.img_ax = self.fig.add_subplot(self.gridspec[0,0])
        self.calculate_button_ax = self.fig.add_subplot(self.gridspec[0,1])

        self.calculateButton = Button(self.calculate_button_ax, "Calculate")

        def calculate(*args):
            filename = self.get_filename()
            img = self.generate_img(filename)
            self.img_ax.imshow(img)
        self.calculateButton.on_clicked(calculate)

    def run(self):
        logging.basicConfig(filename='log.log', level=logging.INFO)
        logging.info(f"started execution at {datetime.datetime.now()}")

        plt.show()

        file_name = self.get_filename()
        img = self.generate_img(file_name)

        plt.imshow(img, interpolation='bicubic')
        plt.show()

    def get_filename(self):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="../", title="Select file",
                                                   filetypes=[("SVG-Image", "*.svg"), ("png image", "*.png"),
                                                              ("jpg image", "*.jpg *.jpeg"),
                                                              ("tagged image file", "*.tiff *.tif"),
                                                              ("All files", "*.*")])
        logging.info(f"Acquired file name")
        return root.filename

    def generate_img(self, filename):
        with open("Themes/neighbor.json") as file:
            js = json.load(file)
        action_dict = {key: SurfaceInfoNoContext.from_json(js[key]) for key in js.keys()}
        logging.info("Loaded action dict")

        loader = Loader()
        shapes = loader.load(filename)
        interpreter = Interpreter()
        hierarchy = interpreter.interpret(shapes)
        theme = Theme()
        interpreter.determine_kind(hierarchy, shapes, theme)
        painter = Painter()
        viewing_window = pygame.Rect(0, 0, 500, 500)
        return painter.paint(hierarchy, shapes, viewing_window, action_dict)



