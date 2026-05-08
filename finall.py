from PIL import Image


image = Image.open ("monro.jpg")
red, green, blue = image.split()



image = Image.open ("red.jpg")                                     
coordinates = (200, 0, image.width, image.height)  
cropped = image.crop (coordinates) 

image = Image.open ("red.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)

image1 = Image.open ("red_cropped.jpg")
image2 = Image.open ("red_mid.jpg")
image3 = Image.blend (image1,image2,0.5)



image = Image.open ("blue.jpg")
coordinates = (0, 0, image.width - 200, image.height )
cropped = image.crop (coordinates)

image = Image.open ("blue.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)

image1 = Image.open ("blue_cropped.jpg")
image2 = Image.open ("blue_mid.jpg")
image3 = Image.blend (image1,image2,0.5)
image3.save ("blendmonroblue.jpg")



image = Image.open ("green.jpg")
coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)



result= Image.merge ("RGB" , ( red , green , blue  ))
result.save ("finalmonro.jpg")



image = Image.open ("finalmonro.jpg")
image.thumbnail ((80, 80))
image.save ("smallfinalmonro.jpg")





