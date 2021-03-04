import logging

from src.Interface import Interface

if __name__ == "__main__":
    try:
        gui = Interface()
        gui.run()
    except Exception as e:
        print("YEEEEEEEE")
        logging.error(e)
