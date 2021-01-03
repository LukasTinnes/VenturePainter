import xml.etree.ElementTree as ET
import planar


class Loader(object):
    """
    The Loader class loads an SVG file and translates it into Shape objects of the Engine
    """

    def __init__(self, path):
        """
        Initialises the loader for a given folder
        :param path: Path to the svg image that is to be painted
        """
        self.path = path
        self.id_count = 0

    def load(self, filename):
        """
        Loads every child node of the root of a specific svg images' xml tree representation
        :param filename: filename of the svg image (in the resource folder)
        """
        #TODO fileending descrimination
        return self._load_svg(filename)

    def _load_svg(self, filename):
        tree = ET.parse(self.path + filename)
        root = tree.getroot()

        # Load information on background size
        root_attrib = root.attrib
        root_width = float(root_attrib["width"])
        root_height = float(root_attrib["height"])

        """Load shapes"""
        shapes = []

        # Create bounding boxes from children
        for child in root:
            # TODO other shapes
            # Extract parameters
            child_attrib = child.attrib
            child_x = float(child_attrib["x"])
            child_y = float(child_attrib["y"])
            child_width = float(child_attrib["width"])
            child_height = float(child_attrib["height"])

            # Build BBox
            maximum = planar.Vec2(child_x + child_width, child_y + child_height)
            minimum = planar.Vec2(child_x, child_y)
            box = planar.BoundingBox([minimum, maximum])

            # Append to shappe list
            shapes.append(box)
        return shapes
