from PIL import Image

image = Image.open ("monro.jpg")
red, green, blue = image.split()

red_coordinates = (200, 0, red.width, red.height)
red_cropped = red.crop (red_coordinates) 

red_coordinates = (100, 0, red.width-100, red.height) 
red_cropped = red.crop (red_coordinates) 

blue_coordinates = (0, 0, blue.width - 200, blue.height)
biue_cropped = blue.crop (blue_coordinates)

blue_coordinates = (100, 0, blue.width-100, blue.height) 
biue_cropped = blue.crop (blue_coordinates)

green_coordinates = (100, 0, green.width-100, green.height) 

result= Image.merge ("RGB" , ( red , green , blue  ))

image.thumbnail ((80, 80))
image.save ("smallfinalmonroo.jpg")
