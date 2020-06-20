from random import randint


def gen_random_picture(width, height, number, name):
    colors = ["red", "blue", "yellow", "green"]
    with open(str.format("chaossvg{}.svg", name), "w+") as image:
        image.writelines(str.format('<svg width="{0}" height="{1}" xmlns="http://www.w3.org/2000/svg">\n', width, height))
        x = 0
        while x < number:
            # Get random attributes
            rand_pos = (randint(0, width), randint(0, height))
            rand_width = randint(0, width)
            rand_height = randint(0, height)
            rand_color = colors[randint(0, 3)]
            # If object would overflow, ignore that one
            if rand_pos[0] + rand_width > width or rand_pos[1] + rand_height > height:
                pass
            else:
                image.writelines(str.format(
                    '\t<rect id="svg_{0}" height="{1}" width="{2}" y="{3}" x="{4}" stroke-width="1.5" stroke="#000" '
                    'fill="{5}"/>\n',
                    x, rand_height, rand_width, rand_pos[0], rand_pos[1], rand_color))
                x += 1
        image.writelines('</svg>')


gen_random_picture(1920, 1080, 50, "cock")
