import datetime
import json
import logging
import os
from tkinter import *
from tkinter import filedialog

import cv2
import matplotlib
import pygame
from matplotlib.image import imsave

from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter
from src.SurfaceInfos.SurfaceInfoArithContext import SurfaceInfoArithContext
from src.SurfaceInfos.SurfaceInfoContext import SurfaceInfoContext
from src.SurfaceInfos.SurfaceInfoNoContext import SurfaceInfoNoContext
from src.Themes.NeighborTheme import NeighborTheme
from src.Themes.SizeRatioTheme import SizeRatioTheme
from src.Themes.SizeTheme import SizeTheme
from src.Themes.TransformationTheme import TransformationTheme
from src.Themes.UniformTheme import UniformTheme

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
        self.theme = UniformTheme()
        self.shapes = None
        self.hierarchy = None
        self.action_dict = None

        # GUI Elements
        self.radio_labels = ["Uniform", "Neighbor", "Size", "SizeRatio", "Transformation"]
        self.fig = plt.figure()
        self.gridspec = gridspec.GridSpec(5, 2, height_ratios=[0.1, 0.1, 0.1, 0.1, 0.9], width_ratios=[0.9, 0.1])

        self.img_ax = self.fig.add_subplot(self.gridspec[:, 0])
        self.paint_button_ax = self.fig.add_subplot(self.gridspec[2, 1])
        self.img_load_button_ax = self.fig.add_subplot(self.gridspec[0, 1])
        self.theme_load_button_ax = self.fig.add_subplot(self.gridspec[1, 1])
        self.save_button_ax = self.fig.add_subplot(self.gridspec[3, 1])
        self.radio_button_ax = self.fig.add_subplot(self.gridspec[4, 1])

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
            path, extension = os.path.splitext(filename)
            # Some day I am going to add svg shit
            if not extension == ".svg":
                im = cv2.imread(filename)
                self.img_ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))

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
            elif self.radio_buttons.value_selected == 1:
                self.theme = NeighborTheme()
            elif self.radio_buttons.value_selected == 2:
                self.theme = SizeTheme()
            elif self.radio_buttons.value_selected == 3:
                self.theme = SizeRatioTheme()
            else:
                self.theme = TransformationTheme()

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
        action_dict = {}
        for key in js.keys():
            surfaceInfo = js[key]
            if surfaceInfo["kind"] == "NoContext":
                action_dict[key] = SurfaceInfoNoContext.from_json(js[key])
            elif surfaceInfo["kind"] == "Context":
                action_dict[key] = SurfaceInfoContext.from_json(js[key])
            elif surfaceInfo["kind"] == "ArithContext":
                action_dict[key] = SurfaceInfoArithContext.from_json(js[key])
        return action_dict

    def paint(self):
        """
        Paint it, black
        :return:
        """
        interpreter = Interpreter()
        interpreter.determine_kind(self.hierarchy, self.shapes, self.theme)
        painter = Painter()
        viewing_window = pygame.Rect(0, 0, 1000, 1000)
        return painter.paint(self.hierarchy, self.shapes, viewing_window, self.action_dict)
