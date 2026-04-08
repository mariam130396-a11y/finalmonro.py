from PIL import Image


image = Image.open ("monro.jpg")
print(image.mode)
red, green, blue = image.split()


red.save("red.jpg")
green.save("green.jpg")
blue.save("blue.jpg")


image = Image.open ("red.jpg")                                     
coordinates = (200, 0, image.width, image.height)  
cropped = image.crop (coordinates) 
cropped.save ("red_cropped.jpg")

image = Image.open ("red.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)
crroped.save ("red_mid.jpg")

image1 = Image.open ("red_cropped.jpg")
image2 = Image.open ("red_mid.jpg")
image3 = Image.blend (image1,image2,0.5)
image3.save ("blendmonro.jpg")



image = Image.open ("blue.jpg")
coordinates = (0, 0, image.width - 200, image.height )
cropped = image.crop (coordinates)
cropped.save ("blue_cropped.jpg")

image = Image.open ("blue.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)
crroped.save ("blue_mid.jpg")

image1 = Image.open ("blue_cropped.jpg")
image2 = Image.open ("blue_mid.jpg")
image3 = Image.blend (image1,image2,0.5)
image3.save ("blendmonroblue.jpg")



image = Image.open ("green.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)
crroped.save ("green_mid.jpg")



red = Image.open ("blendmonro.jpg")
green = Image.open ("green_mid.jpg")
blue = Image.open ("blendmonroblue.jpg")

result= Image.merge ("RGB" , ( red , green , blue  ))
result.save ("finalmonro.jpg")



image = Image.open ("finalmonro.jpg")
image.thumbnail ((80, 80))
image.save ("smallfinalmonro.jpg")





