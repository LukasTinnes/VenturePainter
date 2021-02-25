import logging
import os
import xml.etree.ElementTree as ET
from typing import List

import cv2
import pygame

from src.Shape import Shape


class Loader:
    """
    The Loader class loads an SVG file and translates it into Shape objects of the Engine
    """

    def __init__(self):
        """
        Initialises the loader for a given folder
        """
        self.id_count = 0

    def load(self, filename: str) -> List[Shape]:
        """
        Loads every child node of the root of a specific svg images' xml tree representation
        :param filename: filename of the svg image (in the resource folder)
        """
        # TODO fileending descrimination
        path, extension = os.path.splitext(filename)
        if extension == ".svg":
            return self._load_svg(filename)
        elif extension == ".png" or extension == ".jpg" or extension == ".jpeg":
            return self._load_img(filename)
        else:
            raise Exception(f"Unknown file ending {extension}")

    def _load_svg(self, filename: str) -> List[Shape]:
        """
        Loads Objects from SVG file
        :param filename:
        :return:
        """
        tree = ET.parse(filename)
        root = tree.getroot()

        # Load information on background size
        root_attrib = root.attrib
        root_width = float(root_attrib["width"])
        root_height = float(root_attrib["height"])

        """Load shapes"""
        shapes = []

        # Create bounding boxes from children
        logging.info(f"Detected {len(root)} children. Loading")
        for child in root:
            # TODO other shapes
            # Extract parameters
            child_attrib = child.attrib
            child_x = float(child_attrib["x"])
            child_y = float(child_attrib["y"])
            child_width = float(child_attrib["width"])
            child_height = float(child_attrib["height"])
            child_color = child_attrib["fill"]

            # Build Shape
            box = pygame.Rect(child_x, child_y, child_width, child_height)
            shape = Shape(box, self.id_count)
            self.id_count += 1

            # Append to shape list
            shapes.append(shape)
            logging.info(f"Loaded child {shape}")
        logging.info(f"loaded all children")
        return shapes

    def _load_img(self, filename):
        print(filename)
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Filter for image smoothing if needed
        gray = cv2.bilateralFilter(gray, 10, 50, 50)
        # Canny Edge Detection
        canny_output = cv2.Canny(gray, 100, 200)
        # Try Shape detection by edge detection
        contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # This detects whiter objects from black background
        # From OpenCV Documentation "In OpenCV, finding contours is like finding white object from black background"
        shapes = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            box = pygame.Rect(x, y, w, h)
            shape = Shape(box, self.id_count)
            self.id_count += 1
            shapes.append(shape)
            logging.info(f"Loaded child {shape}")
        logging.info(f"loaded all children")
        return shapes
