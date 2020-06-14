from PIL import Image
import random


class Texture:

    def __init__(self, image):
        self.image = image

    def stochastic(self, dimensions):
        img = Image.new("RGB", dimensions)
        width, height = self.image.size
        pixels_img = self.image.load()
        pixels_new_img = img.load()

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                x_rand = random.randint(0, width - 1)
                y_rand = random.randint(0, height - 1)
                pixels_new_img[x, y] = pixels_img[x_rand, y_rand]

        return img

    def tiles(self, dimensions):
        img = Image.new("RGB", dimensions)
        print(int(dimensions[0] / self.image.size[0]), int(dimensions[1] / self.image.size[1]))
        for x in range(int(dimensions[0] / self.image.size[0]) + 1):
            for y in range(int(dimensions[1] / self.image.size[1]) + 1):
                img.paste(self.image, (x * self.image.size[0], y * self.image.size[1]))
        return img

    def mirror_tiles(self, dimensions):
        img = Image.new("RGB", dimensions)
        print(int(dimensions[0] / self.image.size[0]), int(dimensions[1] / self.image.size[1]))
        for x in range(int(dimensions[0] / self.image.size[0])):
            for y in range(int(dimensions[1] / self.image.size[1])):
                to_paste = self.image
                if x % 2 == 1:
                    to_paste = to_paste.transpose(Image.FLIP_LEFT_RIGHT)
                if y % 2 == 1:
                    to_paste = to_paste.transpose(Image.FLIP_TOP_BOTTOM)
                img.paste(to_paste, (x * self.image.size[0], y * self.image.size[1]))
        return img

    def growing(self, dimensions, kernel, seed):
        """
        Image growing algorithm
        :param dimensions:
        :param mask:
        :param seed:
        :return:
        """
        img = Image.new("RGB", dimensions)
        img_crop = self.image.crop(seed)
        img.paste(img_crop, (seed[0], seed[1]))
        pixels = img.load()
        while not (seed[0] == 0 or seed[1] == 0 or seed[2] == dimensions[1] or seed[3] == dimensions[2]):
            pass  # TODO
        return img
