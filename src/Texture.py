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
                x_rand = random.randint(0, width-1)
                y_rand = random.randint(0, height-1)
                pixels_new_img[x,y] = pixels_img[x_rand, y_rand]

        return img

    def tiles(self, dimensions):
        img = Image.new("RGB", dimensions)
        print(int(dimensions[0] / self.image.size[0]), int(dimensions[1] / self.image.size[1]))
        for x in range(int(dimensions[0] / self.image.size[0])):
            for y in range(int(dimensions[1] / self.image.size[1])):
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

    def growing(self, dimensions, kernel, seed, threshold):
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
        pixels_orig = self.image.load()
        while not (seed[0] == 0 and seed[1] == 0 and seed[2] == dimensions[0]-1 and seed[3] == dimensions[1]-1):
            empties = list(self.range_around_box(seed, img))
            for empty in empties:
                empties.remove(empty)
                self.__growing(empty, pixels, pixels_orig, kernel, empties, seed, threshold)

            if not seed[0] == 0:
                seed[0] -= 1
            if not seed[1] == 0:
                seed[1] -= 1
            if not seed[2] == img.size[0]-1:
                seed[2] += 1
            if not seed[3] == img.size[1]-1:
                seed[3] += 1
            print(f"SEED: {seed}")

        return img

    def range_around_box(self, seed, img):
        if not (seed[1] == 0 or seed[0] == 0):
            print("lu")
            yield seed[0] - 1, seed[1] - 1

        if not seed[0] == 0:
            print("left")
            for y in range(seed[1], seed[3] + 1):
                yield seed[0] - 1, y

        if not (seed[3] == img.size[1] - 1 or seed[1] == 0):
            print("ld")
            yield seed[0] - 1, seed[3] + 1

        if not seed[3] == img.size[1] - 1:
            print("down")
            for x in range(seed[0], seed[2] + 1):
                yield x, seed[3] + 1

        if not seed[3] == img.size[1] - 1:
            print("rd")
            yield seed[2] + 1, seed[3] + 1

        if not seed[2] == img.size[1] - 1:
            print("right")
            for y in range(seed[1], seed[3] + 1):
                yield seed[2] + 1, y

        if not (seed[2] == img.size[1] - 1 or seed[1] == 0):
            print("ru")
            yield seed[2] + 1, seed[1] - 1

        if not seed[1] == 0:
            print("up")
            for x in range(seed[0], seed[2] + 1):
                yield x, seed[1] - 1


    def __growing(self, point, pixels_new, pixels_orig, kernel, empties, seed, threshold):
        print(point)
        candidates = []
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                acc = 0
                for mask_x in range(-1, 2):
                    for mask_y in range(-1, 2):
                        if not (point[0] + mask_x < seed[0] or point[1] + mask_y < seed[1]):
                            if not (point[0] + mask_x >= seed[2] or point[1] + mask_y >= seed[3]):
                                if not (x + mask_x < 0 or y + mask_y < 0):
                                    if not (x + mask_x >= self.image.size[0] or y + mask_y >= self.image.size[1]):
                                        if not (x + mask_x, y + mask_y) in empties:
                                            col = pixels_new[point[0] + mask_x, point[1] + mask_y]
                                            col2 = pixels_orig[x + mask_x, y + mask_y]
                                            farbe = ((col[0] + col2[0]) * kernel[mask_x+1, mask_y+1],
                                                     (col[1] + col2[1]) * kernel[mask_x + 1, mask_y + 1],
                                                     (col[2] + col2[2]) * kernel[mask_x + 1, mask_y + 1])
                                            acc += (farbe[0] + farbe[1] + farbe[2]) / 3
                if acc < threshold:
                    candidates.append((x, y))
        winner = random.choice(candidates)
        pixels_new[point[0], point[1]] = pixels_orig[winner[0], winner[1]]
