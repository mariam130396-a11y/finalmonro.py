from PIL import Image


image = Image.open("monro.jpg")
red, green, blue = image.split()


red = Image.blend(
    red.crop((200, 0, red.width, red.height)),
    red.crop((100, 0, red.width - 100, red.height)),
    0.5
)


blue = Image.blend(
    blue.crop((0, 0, blue.width - 200, blue.height)),
    blue.crop((100, 0, blue.width - 100, blue.height)),
    0.5
)


green = green.crop((100, 0, green.width - 100, green.height))


result = Image.merge("RGB", (red, green, blue))
result.save("finalmonro.jpg")


result.thumbnail((80, 80))
result.save("smallfinalmonro.jpg")