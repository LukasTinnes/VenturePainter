import math
import random
import numpy as np
import math
from noise.perlin import SimplexNoise

class Texture:

    def __init__(self, image):
        self.image = image

    @staticmethod
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
    def simplexNoise(dimensions, scale_x=1, scale_y=1):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                color = (SimplexNoise().noise2(x/scale_x, y/scale_y)+1)/2
                img[x, y] = np.array([color]*3)
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
    def sine_perlin(dimensions, perlin_scale=1, sine_scale=1, randomness=0):
        """
        Makes a salt and pepper texture using multiple colors with the same proability
        :param dimensions: The Textures dimensions
        :param condiments: The colors to choose from
        """

        img = np.empty((dimensions[0], dimensions[1], 3))

        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                perlin = (SimplexNoise().noise2(x / perlin_scale, y / perlin_scale) + 1)*randomness
                sine = (math.sin(x*sine_scale+perlin)+1)/2
                img[x, y] = np.array([sine]*3)
        return img

    def tiles(self, dimensions):
        """
        Copy pastes the images as tiles
        :param dimensions:
        :return:
        """
        img = Image.new("RGB", dimensions)
        print(int(dimensions[0] / self.image.size[0]), int(dimensions[1] / self.image.size[1]))
        for x in range(math.ceil(dimensions[0] / self.image.size[0])):
            for y in range(math.ceil(dimensions[1] / self.image.size[1])):
                img.paste(self.image, (x * self.image.size[0], y * self.image.size[1]))
        return img

    def mirror_tiles(self, dimensions):
        img = Image.new("RGB", dimensions)
        print(int(dimensions[0] / self.image.size[0]), int(dimensions[1] / self.image.size[1]))
        for x in range(math.ceil(dimensions[0] / self.image.size[0])):
            for y in range(math.ceil(dimensions[1] / self.image.size[1])):
                to_paste = self.image
                if x % 2 == 1:
                    to_paste = to_paste.transpose(Image.FLIP_LEFT_RIGHT)
                if y % 2 == 1:
                    to_paste = to_paste.transpose(Image.FLIP_TOP_BOTTOM)
                img.paste(to_paste, (x * self.image.size[0], y * self.image.size[1]))
        return img

    def quilting(self, dimensions, quilt_dimensions):
        """
        Implements quilting algorithm, defined in https://people.eecs.berkeley.edu/~efros/research/quilting/quilting.pdf
        :param dimensions:
        :param quilt_dimensions:
        :return:
        """
        img = Image.new("RGB", dimensions, (0xFF, 0x00, 0xFF))
        img_quilt_ratio_x = int(dimensions[0] / quilt_dimensions[0])
        img_quilt_ratio_y = int(dimensions[1] / quilt_dimensions[1])
        for x in range(img_quilt_ratio_x):
            for y in range(img_quilt_ratio_y):
                quilt_x, quilt_y = self.quilt_x_y(quilt_dimensions)
                crop = self.image.crop((quilt_x, quilt_y, quilt_x + quilt_dimensions[0], quilt_y + quilt_dimensions[1]))
                img.paste(crop, (x * quilt_dimensions[0], y * quilt_dimensions[1], (x + 1) * quilt_dimensions[0],
                                 (y + 1) * quilt_dimensions[1]))
        return img

    def quilt_x_y(self, quilt_dimensions):
        """
        quilt_x and quilt_y
        :param quilt_dimensions: quilt_dimensions
        :return: quilt_x and quilt_y
        """
        quilt_x = random.randint(0, self.image.size[0] - 1 - quilt_dimensions[0])
        quilt_y = random.randint(0, self.image.size[1] - 1 - quilt_dimensions[1])
        return quilt_x, quilt_y

    def quilting_overlay(self, dimensions, quilt_dimensions, overlay=0):  # TODO Is bugged needs to be parallelized
        img = Image.new("RGB", dimensions, (0xFF, 0x00, 0xFF))
        img_quilt_ratio_x = int(dimensions[0] / (quilt_dimensions[0] - overlay))
        img_quilt_ratio_y = int(dimensions[1] / (quilt_dimensions[1] - overlay))
        for x in range(img_quilt_ratio_x):
            for y in range(img_quilt_ratio_y):
                print("Quilt", x, y, img_quilt_ratio_x, img_quilt_ratio_y)
                if x == 0 and y == 0:
                    quilt_x, quilt_y = self.quilt_x_y(quilt_dimensions)
                    crop = self.image.crop(
                        (quilt_x, quilt_y, quilt_x + quilt_dimensions[0], quilt_y + quilt_dimensions[1]))
                else:
                    crop = None
                    final_error = math.inf
                    f_x = -1
                    f_y = -1
                    for x_comp in range(self.image.size[0] - quilt_dimensions[0]):
                        for y_comp in range(self.image.size[1] - quilt_dimensions[1]):
                            comparison_quilt = self.image.crop(
                                (x_comp, y_comp, x_comp + quilt_dimensions[0], y_comp + quilt_dimensions[1]))
                            comp_pix = comparison_quilt.load()
                            img_pix = img.load()

                            error_left = 0
                            error_up = 0

                            if x > 0:
                                for x_ssd in range(overlay):
                                    for y_ssd in range(quilt_dimensions[1]):
                                        error_r = (comp_pix[x_ssd, y_ssd][0] -
                                                   img_pix[quilt_dimensions[0] - 1 - overlay + x_ssd, y_ssd][0]) ** 2
                                        error_g = (comp_pix[x_ssd, y_ssd][1] -
                                                   img_pix[quilt_dimensions[0] - 1 - overlay + x_ssd, y_ssd][1]) ** 2
                                        error_b = (comp_pix[x_ssd, y_ssd][2] -
                                                   img_pix[quilt_dimensions[0] - 1 - overlay + x_ssd, y_ssd][2]) ** 2
                                        error_left += (error_r + error_g + error_b) / 3
                                error_left /= overlay * quilt_dimensions[1]
                            if y > 0:
                                for x_ssd in range(quilt_dimensions[0]):
                                    for y_ssd in range(overlay):
                                        error_r = (comp_pix[x_ssd, y_ssd][0] -
                                                   img_pix[x_ssd, quilt_dimensions[1] - 1 - overlay + y_ssd][0]) ** 2
                                        error_g = (comp_pix[x_ssd, y_ssd][1] -
                                                   img_pix[x_ssd, quilt_dimensions[1] - 1 - overlay + y_ssd][1]) ** 2
                                        error_b = (comp_pix[x_ssd, y_ssd][2] -
                                                   img_pix[x_ssd, quilt_dimensions[1] - 1 - overlay + y_ssd][2]) ** 2
                                        error_up += (error_r + error_g + error_b) / 3
                                error_up /= overlay * quilt_dimensions[1]
                            error = error_up + error_left
                            if error < final_error:
                                final_error = error
                                crop = comparison_quilt
                                f_x = x_comp
                                f_y = y_comp
                    print("Final Error", final_error)
                    print("f", f_x, f_y)
                img.paste(crop, (x * quilt_dimensions[0], y * quilt_dimensions[1], (x + 1) * quilt_dimensions[0],
                                 (y + 1) * quilt_dimensions[1]))
        return img

    def growing(self, dimensions, kernel, seed, threshold):
        """
        Image growing algorithm
        :param dimensions:
        :param seed:
        :param kernel
        :param threshold
        :return:
        """
        img = Image.new("RGB", dimensions, (0xFF, 0x00, 0xFF))
        # img = Image.new("L", dimensions, (0xFF,))
        img_crop = self.image.crop((seed[0], seed[1], seed[2] + 1, seed[3] + 1))
        img.paste(img_crop, (seed[0], seed[1]))
        img.show()
        pixels = img.load()
        pixels_orig = self.image.load()
        while not (seed[0] == 0 and seed[1] == 0 and seed[2] == dimensions[0] - 1 and seed[3] == dimensions[1] - 1):
            empties = list(self.range_around_box(seed, img))
            print(f"Empties: {empties}")
            for empty in self.range_around_box(seed, img):
                empties.remove(empty)
                self.__growing(empty, pixels, pixels_orig, kernel, empties, seed, threshold, dimensions)

            if not seed[0] == 0:
                seed[0] -= 1
            if not seed[1] == 0:
                seed[1] -= 1
            if not seed[2] == img.size[0] - 1:
                seed[2] += 1
            if not seed[3] == img.size[1] - 1:
                seed[3] += 1
            print(f"SEED: {seed}")

        return img

    @staticmethod
    def range_around_box(seed, img):
        if not (seed[1] == 0 or seed[0] == 0):
            yield seed[0] - 1, seed[1] - 1

        if not seed[0] == 0:
            for y in range(seed[1], seed[3] + 1):
                yield seed[0] - 1, y

        if not (seed[3] == img.size[1] - 1 or seed[1] == 0):
            yield seed[0] - 1, seed[3] + 1

        if not seed[3] == img.size[1] - 1:
            for x in range(seed[0], seed[2] + 1):
                yield x, seed[3] + 1

        if not seed[3] == img.size[1] - 1:
            yield seed[2] + 1, seed[3] + 1

        if not seed[2] == img.size[1] - 1:
            for y in range(seed[1], seed[3] + 1):
                yield seed[2] + 1, y

        if not (seed[2] == img.size[1] - 1 or seed[1] == 0):
            yield seed[2] + 1, seed[1] - 1

        if not seed[1] == 0:
            for x in range(seed[0], seed[2] + 1):
                yield x, seed[1] - 1

    def __growing(self, point, pixels_new, pixels_orig, kernel, empties, seed, threshold, dimensions):
        candidates = []
        # print("growing")
        overall_color = (0, 0, 0)
        # overall_color = 0
        print(point)
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                acc = 0
                mask_acc = 0
                for mask_x in range(-int(kernel.shape[0] / 2), int(kernel.shape[0] / 2) + 1):
                    for mask_y in range(-int(kernel.shape[1] / 2), int(kernel.shape[1] / 2) + 1):
                        if not (point[0] + mask_x < seed[0] or point[1] + mask_y < seed[1]):
                            if not (point[0] + mask_x > seed[2] or point[1] + mask_y > seed[3]):
                                if not (x + mask_x < 0 or y + mask_y < 0):
                                    if not (x + mask_x >= self.image.size[0] or y + mask_y >= self.image.size[1]):
                                        if not (point[0] + mask_x, point[1] + mask_y) in empties:
                                            mask_acc += 1
                                            x_new, y_new = point[0] + mask_x, point[1] + mask_y
                                            col = pixels_new[x_new, y_new]
                                            # if col[0] == 0xFF and col[1] == 0x00 and col[2] == 0xFF:
                                            #    print("Something fucky")
                                            col2 = pixels_orig[x + mask_x, y + mask_y]
                                            # overall_color = overall_color + abs(col - col2) * kernel[mask_x + int(kernel.shape[0]/2), mask_y + int(kernel.shape[0]/2)]
                                            overall_color = (overall_color[0] + abs(col[0] - col2[0]) * kernel[
                                                mask_x + int(kernel.shape[0] / 2), mask_y + int(kernel.shape[0] / 2)],
                                                             overall_color[1] + abs(col[1] - col2[1]) * kernel[
                                                                 mask_x + int(kernel.shape[0] / 2), mask_y + int(
                                                                     kernel.shape[0] / 2)],
                                                             overall_color[2] + abs(col[2] - col2[2]) * kernel[
                                                                 mask_x + int(kernel.shape[0] / 2), mask_y + int(
                                                                     kernel.shape[0] / 2)])

                        acc += (overall_color[0] + overall_color[1] + overall_color[2]) / 3
                        # acc += overall_color
                        overall_color = (0, 0, 0)
                        # overall_color = 0

                if acc < threshold and mask_acc > 0:
                    # print(f"Acc: {acc}")
                    candidates.append((x, y))

        winner = random.choice(candidates)
        pixels_new[point[0], point[1]] = pixels_orig[winner[0], winner[1]]
