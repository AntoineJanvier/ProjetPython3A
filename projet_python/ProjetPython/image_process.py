from PIL import Image


def img_proc(img, im, type_wanted):
    if type_wanted == "RED":
        # RED FILTER
        #
        cop = im.copy()
        w, h = cop.size
        pix = cop.load()
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                r = 255
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_red." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_red." + img.file.url.split('.')[1]
    elif type_wanted == "GREEN":
        # GREEN FILTER
        #
        cop = im.copy()
        w, h = cop.size
        pix = cop.load()
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                g = 255
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_green." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_green." + img.file.url.split('.')[1]

    elif type_wanted == "BLUE":
        # BLUE FILTER
        #
        cop = im.copy()
        w, h = cop.size
        pix = cop.load()
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                b = 255
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_blue." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_blue." + img.file.url.split('.')[1]

    elif type_wanted == "LUM1":
        # LUMINOSITY 1
        #
        cop = im.copy()
        pix = cop.load()
        w, h = cop.size
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                r = r / 2
                g = g / 2
                b = b / 2
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_lum1." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_lum1." + img.file.url.split('.')[1]

    elif type_wanted == "LUM2":
        # LUMINOSITY 2
        #
        cop = im.copy()
        pix = cop.load()
        w, h = cop.size
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                r = r * 2
                g = g * 2
                b = b * 2
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_lum2." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_lum2." + img.file.url.split('.')[1]
    elif type_wanted == "INVERTED":
        # INVERTED COLORS
        #
        cop = im.copy()
        w, h = cop.size
        pix = cop.load()
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                r = 255 - r
                g = 255 - g
                b = 255 - b
                pix[i, j] = r, g, b
        cop.save(img.file.path.split('.')[0] + "_inverted." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_inverted." + img.file.url.split('.')[1]
    elif type_wanted == "GREY":
        # SHADES OF GREY
        #
        w, h = im.size
        gray = Image.new("L", (w, h))
        pix2 = gray.load()

        cop = im.copy()
        pix = cop.load()
        w, h = cop.size
        for i in range(0, w):
            for j in range(0, h):
                r, g, b = pix[i, j]
                sum = int((r + g + b) / 3)
                pix2[i, j] = sum

        gray.save(img.file.path.split('.')[0] + "_gray." + img.file.path.split('.')[1])
        return img.file.url.split('.')[0] + "_gray." + img.file.url.split('.')[1]
    else:
        return ""
