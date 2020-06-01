from src.Loader import Loader

if __name__ == "__main__":
    loader = Loader("../Resources/")
    shapes = loader.load("complex.svg")
