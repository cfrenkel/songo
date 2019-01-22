import PIL

from PIL import Image, ImageOps

def create_collage_9(imgs):
    target_img = Image.new("RGB", (600, 600))

    for i in range(9):
        imgs[i] = imgs[i].resize((200, 200))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 200))
    target_img.paste(imgs[2], (200, 0))
    target_img.paste(imgs[3], (200, 200))
    target_img.paste(imgs[4], (400, 0))
    target_img.paste(imgs[5], (0, 400))
    target_img.paste(imgs[6], (200, 400))
    target_img.paste(imgs[7], (400, 200))
    target_img.paste(imgs[8], (400, 400))

    return target_img

def small_image(list_image):
    imjlist = []
    for i in list_image:
        img = Image.open(i)
        si = img.size
        img = img.resize((int(si[0] / 3.5), int(si[0] / 3.5)), Image.ANTIALIAS)
        imjlist.append(img)
    return imjlist


def last_screen(list_image):
    lm_list = small_image(list_image)
    return create_collage_9(lm_list)


# a = 'C:\\Users\\שרה ויסברגר\\Pictures\\Camera Roll\\tt.jpg'
# g = [a, a, a, a, a, a, a, a, a]
# last_screen(g)

