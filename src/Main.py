from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter
import logging

if __name__ == "__main__":
    logging.basicConfig(filename='example.log', level=logging.INFO)
    loader = Loader("../Resources/")
    background = loader.load("complex.svg")
    print(background)
    #interpreter = Interpreter()
    #hierarchy = interpreter.interpret(background, shapes)
    #painter = Painter()
    #img = painter.paint(hierarchy, background, shapes, camera)
    #img.show()
