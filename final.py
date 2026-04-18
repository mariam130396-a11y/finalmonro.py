from PIL import Image


image = Image.open ("monro.jpg")
print(image.mode)
red, green, blue = image.split()

                                    
coordinates = (200, 0, image.width, image.height)  
cropped = image.crop (coordinates) 

coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)

coordinates = (0, 0, image.width - 200, image.height )
cropped = image.crop (coordinates)

coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)

coordinates = (100, 0, image.width-100, image.height) 
crroped = image.crop (coordinates)

result= Image.merge ("RGB" , ( red , green , blue  ))

image.thumbnail ((80, 80))
image.save ("smallfinalmonro.jpg")





