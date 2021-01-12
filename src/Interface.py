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
        # Data
        self.img = None
        self.theme = None
        self.shapes = None
        self.hierarchy = None
        self.action_dict = None

        # GUI Elements
        self.radio_labels = ["Uniform", "Neighbor"]
        self.fig = plt.figure()
        self.gridspec = gridspec.GridSpec(5,2, height_ratios=[0.1, 0.1, 0.1, 0.1,0.9], width_ratios=[0.9,0.1])

        self.img_ax = self.fig.add_subplot(self.gridspec[:,0])
        self.paint_button_ax = self.fig.add_subplot(self.gridspec[2,1])
        self.img_load_button_ax = self.fig.add_subplot(self.gridspec[0, 1])
        self.theme_load_button_ax = self.fig.add_subplot(self.gridspec[1, 1])
        self.save_button_ax = self.fig.add_subplot(self.gridspec[3,1])
        self.radio_button_ax = self.fig.add_subplot(self.gridspec[4,1])

        self.radio_buttons = RadioButtons(self.radio_button_ax, self.radio_labels)
        self.imgLoadButton = Button(self.img_load_button_ax, "Load Image")
        self.themeLoadButton = Button(self.theme_load_button_ax, "Load Theme")
        self.paintButton = Button(self.paint_button_ax, "Paint")
        self.saveButton = Button(self.save_button_ax, "Save")

        def img_load(*args):
            filename = self.get_filename([("SVG-Image", "*.svg"), ("png image", "*.png"),
                                           ("jpg image", "*.jpg *.jpeg"),
                                           ("tagged image file", "*.tiff *.tif"),
                                           ("All files", "*.*")], "Select image")
            self.shapes, self.hierarchy = self.load_img(filename)
        self.imgLoadButton.on_clicked(img_load)

        def theme_load(*args):
            self.action_dict = self.load_theme()
        self.themeLoadButton.on_clicked(theme_load)

        def paint(*args):
            self.img = self.paint()
            self.img_ax.imshow(self.img)
        self.paintButton.on_clicked(paint)

        def save(*args):
            if self.img is not None:
                imsave("yee.png", self.img)
                print("saved")

        def on_radio_select(*args):
            if self.radio_buttons.value_selected == 0:
                self.theme = UniformTheme()
            else:
                self.theme = NeighborTheme()
        self.radio_buttons.on_clicked(on_radio_select)
        self.saveButton.on_clicked(save)

    def run(self):
        logging.basicConfig(filename='log.log', level=logging.INFO)
        logging.info(f"started execution at {datetime.datetime.now()}")

        plt.show()

    def get_filename(self, endings, title):
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="../", title=title,
                                                   filetypes=endings)
        logging.info(f"Acquired file name")
        return root.filename

    def load_img(self, filename):
        """
        Loads the image
        :param filename:
        :return:
        """
        loader = Loader()
        shapes = loader.load(filename)
        interpreter = Interpreter()
        hierarchy = interpreter.interpret(shapes)

        return shapes, hierarchy

    def load_theme(self):
        """
        Loads the theme and action dict
        :return:
        """
        file_name = self.get_filename([("json theme", "*.json"), ("All files", "*.*")], "Select theme")
        with open(file_name) as file:
            js = json.load(file)
        action_dict = {key: SurfaceInfoNoContext.from_json(js[key]) for key in js.keys()}
        return action_dict

    def paint(self):
        """
        Paint it, black
        :return:
        """
        interpreter = Interpreter()
        interpreter.determine_kind(self.hierarchy, self.shapes, self.theme)
        painter = Painter()
        viewing_window = pygame.Rect(0, 0, 500, 500)
        return painter.paint(self.hierarchy, self.shapes, viewing_window, self.action_dict)




