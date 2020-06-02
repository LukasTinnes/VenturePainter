from src.Intrepreter import Interpreter
from src.Loader import Loader

if __name__ == "__main__":
    loader = Loader("../Resources/")
    background, shapes = loader.load("complex.svg")
    interpreter = Interpreter()
    interpreter.interpret(background, shapes)
