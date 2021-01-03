import os
from tkinter import *
from tkinter import filedialog

from src.Loader import Loader

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select file",
                                               filetypes=[("SVG-Image", "*.svg"), ("All files", "*.*")])
    folder_path = os.path.dirname(root.filename)
    loader = Loader("../Resources/")
    background, r_w, r_h = loader.load("complex.svg")
    print(background, r_w, r_h)
    # interpreter = Interpreter()
    # hierarchy = interpreter.interpret(background, shapes)
    # painter = Painter()
    # img = painter.paint(hierarchy, background, shapes, camera)
    # img.show()
