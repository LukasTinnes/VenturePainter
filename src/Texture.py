import math
import random
import numpy as np
import math
from noise.perlin import SimplexNoise
from numba import jit
import cv2


class Texture:

    def __init__(self, image):
        self.image = image

    @staticmethod
    @jit()
    def flat(dimensions, color=None):
        if color is None:
            color = np.array([1, 1, 1])

        img = np.empty((dimensions[0], dimensions[1], 3))
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                img[x,y] = color
        return img

    @staticmethod
    @jit()
    def saltAndPepper(dimensions, salt=None, pepper=None, p=0.5):
        """
        Makes a salt and pepper texture using the provided colors.
        :param dimensions: The Textures dimensions
        :param salt: The salt color
        :param pepper: The pepper color
        :param p: The probability that a pixel is salt
        :return:
        """
        if salt is None:
            salt = np.array([0, 0, 0])
        if pepper is None:
            pepper = np.array([1, 1, 1])

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                if random.random() < p:
                    img[x, y] = salt
                else:
                    img[x, y] = pepper
        return img

    @staticmethod
    def condiments(dimensions, condiments):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                img[x, y] = random.choice(condiments)
        return img

    @staticmethod
    def simplexNoise(dimensions, scale_x=1, scale_y=1, salt=None, pepper=None):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """
        salt = np.array([0, 0, 0]) if salt is None else np.array(salt)
        pepper = np.array([1, 1, 1]) if pepper is None else np.array(pepper)

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                color = (SimplexNoise().noise2(x/scale_x, y/scale_y)+1)/2
                img[x, y] = np.array(salt*color+pepper*(1-color))
        return img

    @staticmethod
    def sine(dimensions, scale=1):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                color = (math.sin(x*scale)+1)/2
                img[x, y] = np.array([color]*3)
        return img

    @staticmethod
    def circle(dimensions, scale=1):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                color = (math.cos(x*scale)+math.sin(y*scale)+2)/4
                img[x, y] = np.array([color]*3)
        return img

    @staticmethod
    def circle_perlin(dimensions, circle_scale=1, perlin_scale=1, randomness=1):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                perlin = (SimplexNoise().noise2(x / perlin_scale, y / perlin_scale) + 1) * randomness
                color = (math.cos(x*circle_scale+perlin)+math.sin(y*circle_scale+perlin)+2)/4
                img[x, y] = np.array([color]*3)
        return img

    @staticmethod
    def sine_perlin(dimensions, perlin_scale=1, sine_scale=1, randomness=0, salt=None, pepper=None):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """
        salt = np.array([0, 0, 0]) if salt is None else np.array(salt)
        pepper = np.array([1, 1, 1]) if pepper is None else np.array(pepper)

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                perlin = (SimplexNoise().noise2(x / perlin_scale, y / perlin_scale) + 1)*randomness
                sine = (math.sin(x*sine_scale+perlin)+1)/2
                img[x, y] = np.array(salt*sine+pepper*(1-sine))
        return img

    @staticmethod
    def checkerboard(dimensions, salt=None, pepper=None, size=1):
        """
        Creates a standarc checkerboard pattern of size size and checks og color salt and pepper.
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """
        salt = np.array([0, 0, 0]) if salt is None else np.array(salt)
        pepper = np.array([1, 1, 1]) if pepper is None else np.array(pepper)
        img = np.empty((dimensions[0], dimensions[1], 3))
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                img[x, y] = salt if (x%(size*2) - size < 0) ^ (y%(size*2) - size < 0) else pepper
        return img

    @staticmethod
    def quilting(dimensions, filename):
        ref_img = cv2.imread(filename)
        ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                img[x, y] = ref_img[x%ref_img.shape[0],y%ref_img.shape[1]] / 255

        return img

    @staticmethod
    def mirror_quilting(dimensions, filename):
        ref_img = cv2.imread(filename)
        ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)

        img = np.empty((dimensions[0], dimensions[1], 3))


        for x in range(dimensions[0]):
            x_sign = x % (ref_img.shape[0]*2)
            if x_sign > ref_img.shape[0]-1:
                x_sign = ref_img.shape[0]-1 - x_sign
            for y in range(dimensions[1]):
                y_sign = y % (ref_img.shape[1] * 2)
                if y_sign > ref_img.shape[1] - 1:
                    y_sign = ref_img.shape[1] - 1 - y_sign
                img[x, y] = ref_img[x_sign,
                                    y_sign] / 255

        return img

    @staticmethod
    def random_block_quilting(dimensions, filename, block_size=None):
        ref_img = cv2.imread(filename)
        ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)

        if block_size is None:
            block_size = int(min(ref_img.shape)/10)

        img = np.ones((dimensions[0], dimensions[1], 3))
        # For each block
        for x_block in range(math.ceil(img.shape[0] / block_size)):
            for y_block in range(math.ceil(img.shape[1] / block_size)):
                # Calculate a starting point for a random block
                random_x = random.randint(0, ref_img.shape[0] - block_size)
                random_y = random.randint(0, ref_img.shape[1] - block_size)
                # Fpr each pixel in the block
                for x in range(block_size):
                    for y in range(block_size):
                        # If the block is in the image, paste the pixel to it.
                        if x+x_block*block_size < img.shape[0] and y+y_block*block_size < img.shape[1]:
                            img[x+x_block*block_size, y+y_block*block_size,:] = ref_img[random_x + x, random_y + y,:] / 255

        return img

    @staticmethod
    def neighbor_block_quilting(dimensions, filename, block_size=None, border_size=1, iterations=5):
        ref_img = cv2.imread(filename)
        ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)

        if block_size is None:
            block_size = int(min(ref_img.shape)/10)

        virtual_block_size = block_size + border_size*2

        img = np.zeros((dimensions[0], dimensions[1], 3))

        # For each block in the image
        for x_block in range(math.ceil(img.shape[0] / block_size)):
            for y_block in range(math.ceil(img.shape[1] / block_size)):
                minimal_energy = math.inf
                minimal_block = None
                # Do <iterations> iterations to find the perfect block to insert form the reference
                for iteration in range(iterations):
                    energy = 0
                    random_x = random.randint(0, ref_img.shape[0] - virtual_block_size)
                    random_y = random.randint(0, ref_img.shape[1] - virtual_block_size)
                    # Find the energy on the edges of the block
                    for x in range(virtual_block_size):
                        for y in range(virtual_block_size):
                            # Don't collect energy of indices bexonde the border
                            if x+x_block*block_size < img.shape[0] and y+y_block*block_size < img.shape[1]:
                                # Don't collect energy not on the edges and account for edge blocks
                                if (x < border_size and x_block > 0) or (y < border_size and y_block > 0):
                                    rgb_energy = abs(img[x+x_block*block_size, y+y_block*block_size, :] -
                                                  ref_img[random_x + x, random_y + y, :] / 255)
                                    energy += rgb_energy.sum()
                    # Is the computed block better than the previous ones.
                    if energy < minimal_energy:
                        minimal_energy = energy
                        minimal_block = (random_x, random_y)

                # Paste the best block to the image
                for x in range(virtual_block_size):
                    for y in range(virtual_block_size):
                        if x + x_block * block_size < img.shape[0] and y + y_block * block_size < img.shape[1]:
                            img[x + x_block * block_size, y + y_block * block_size, :] = \
                                ref_img[minimal_block[0] + x, minimal_block[1] + y, :] / 255

        return img

    @staticmethod
    def strech_img(dimensions, filename):
        ref_img = cv2.imread(filename)
        ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB) / 255

        img = np.zeros((dimensions[0], dimensions[1], 3))
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                ref_x = int(x / img.shape[0] * ref_img.shape[0])
                ref_y = int(y / img.shape[1] * ref_img.shape[1])

                img[x,y] = ref_img[ref_x, ref_y]

        return img
