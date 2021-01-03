from src.Intrepreter import Interpreter
from src.Loader import Loader
from src.Painter import Painter

if __name__ == "__main__":
    loader = Loader("../Resources/")
    background, r_w, r_h = loader.load("complex.svg")
    print(background, r_w, r_h)
    #interpreter = Interpreter()
    #hierarchy = interpreter.interpret(background, shapes)
    #painter = Painter()
    #img = painter.paint(hierarchy, background, shapes, camera)
    #img.show()
