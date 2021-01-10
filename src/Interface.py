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
from src.Themes.UniformTheme import UniformTheme
from src.Themes.NeighborTheme import NeighborTheme
import matplotlib
from matplotlib.image import imsave
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.widgets import Button, RadioButtons
from matplotlib import gridspec


class Interface:
    """
    The general Interface class for the project.
    """

    def __init__(self):
        # GUI Elements
        self.radio_labels = ["Uniform", "Neighbor"]

        self.img = None

        self.fig = plt.figure()
        self.gridspec = gridspec.GridSpec(3,2, height_ratios=[0.1, 0.1, 0.9], width_ratios=[0.9,0.1])

        self.img_ax = self.fig.add_subplot(self.gridspec[:,0])
        self.calculate_button_ax = self.fig.add_subplot(self.gridspec[0,1])
        self.save_button_ax = self.fig.add_subplot(self.gridspec[1,1])
        self.radio_button_ax = self.fig.add_subplot(self.gridspec[2,1])

        self.radio_buttons = RadioButtons(self.radio_button_ax, self.radio_labels)
        self.calculateButton = Button(self.calculate_button_ax, "Calculate")
        self.saveButton = Button(self.save_button_ax, "Save")

        def calculate(*args):
            filename = self.get_filename()
            self.img = self.generate_img(filename)
            self.img_ax.imshow(self.img)
        self.calculateButton.on_clicked(calculate)

        def save(*args):
            if self.img is not None:
                imsave("yee.png", self.img)
                print("saved")
        self.saveButton.on_clicked(save)


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
        theme, js = self.get_theme()
        action_dict = {key: SurfaceInfoNoContext.from_json(js[key]) for key in js.keys()}
        logging.info("Loaded action dict")

        loader = Loader()
        shapes = loader.load(filename)
        interpreter = Interpreter()
        hierarchy = interpreter.interpret(shapes)


        interpreter.determine_kind(hierarchy, shapes, theme)
        painter = Painter()
        viewing_window = pygame.Rect(0, 0, 500, 500)
        return painter.paint(hierarchy, shapes, viewing_window, action_dict)

    def get_theme(self):
        if self.radio_buttons.value_selected == self.radio_labels[0]:
            with open("Themes/uniform.json") as file:
                js = json.load(file)
            return UniformTheme(), js
        elif self.radio_buttons.value_selected == self.radio_labels[1]:
            with open("Themes/neighbor.json") as file:
                js = json.load(file)
            return NeighborTheme(), js
        else:
            raise Exception("Radio value that doesn't exist!")


