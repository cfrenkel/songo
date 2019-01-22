import PIL

from PIL import Image


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

def create_collage_1(imgs):

    target_img = Image.new("RGB", (0, 600))
    target_img.paste(imgs[0], (0, 0))
    return target_img

def create_collage_2(imgs):
    target_img = Image.new("RGB", (600, 1200))

    for i in range(2):
        imgs[i] = imgs[i].resize((200, 200))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 600))

    return target_img

def create_collage_3(imgs):
    target_img = Image.new("RGB", (600, 1800))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 600))
    target_img.paste(imgs[2], (0, 1200))

    return target_img

def create_collage_4(imgs):
    target_img = Image.new("RGB", (600, 2400))

    #     for i in range(3):
    #         imgs[i] = imgs[i].resize((300, 300))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 600))
    target_img.paste(imgs[2], (0, 1200))
    target_img.paste(imgs[3], (0, 1800))

    return target_img

def small_image(list_image):
    imjlist = []
    for i in list_image:
        img = Image.open(i)
        si = img.size
        img = img.resize((int(si[0] / 1.5), int(si[0] / 1.5)), Image.ANTIALIAS)
        imjlist.append(img)
    return imjlist

def faces(list_image, x):
    # lm_list = small_image(list_image)
    lm_list = list_image
    if x == 1:
        return create_collage_1(lm_list)
    if x == 2:
        return create_collage_2(lm_list)
    if x == 3:
        return create_collage_3(lm_list)
    if x == 4:
        return create_collage_4(lm_list)





