from PIL import Image, ImageStat, ImageFilter


class ImgTest:

    def __init__(self, path):
        self.img = Image.open(path)
        print(self.img)
        self.img.show()
        stat = ImageStat.Stat(self.img)
        hist = self.img.histogram()
        R = hist[:256]
        G = hist[256:256*2]
        B = hist[256*2:256*3]
        print(
              f"Image Information:\n"
              f"Histogram:\n"
              f"\tR:{R}\n"
              f"\tG:{G}\n"
              f"\tB:{B}\n"
              f"Extrema: {stat.extrema}\n"
              f"Count: {stat.count}\n"
              f"Sum: {stat.sum}\n"
              f"Sum2: {stat.sum2}\n"
              f"Mean: {stat.mean}\n"
              f"RMS: {stat.rms}\n"
              f"Var: {stat.var}\n"
              f"Stddev: {stat.stddev}\n"
              f"Entropy: {self.img.entropy()}"
              )
        RELIEF = [-2, -1, 0, -1, 1, 1, 0, 1, 2]
        SOEBEL = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
        edge = ImageFilter.EDGE_ENHANCE()
        filter = ImageFilter.Kernel(size=(3,3), scale=1/9, offset=50, kernel=SOEBEL)
        print(edge.filterargs)
        img_new = self.img.filter(filter)
        img_new.show()


ImgTest(r"..\..\Resources\marble.png")
