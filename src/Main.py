from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter

if __name__ == "__main__":
    loader = Loader("../Resources/")
    background, shapes = loader.load("test.svg")
    interpreter = Interpreter()
    hierarchy = interpreter.interpret(background, shapes)
    painter = Painter()
    img = painter.paint(hierarchy, background, shapes, (200,200))
    img.show()
