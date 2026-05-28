from PIL import Image

image = Image.open ("monro.jpg")
red, green, blue = image.split()

red_coordinates_1 = (200, 0, red.width, red.height)
red_cropped_1 = red.crop (red_coordinates_1) 

red_coordinates_2 = (100, 0, red.width-100, red.height) 
red_cropped_2 = red.crop (red_coordinates_2) 

redmix = Image.blend (red_cropped_1, red_cropped_2 , 0.5)

blue_coordinates_1 = (0, 0, blue.width - 200, blue.height)
blue_cropped_1 = blue.crop (blue_coordinates_1)

blue_coordinates_2 = (100, 0, blue.width-100, blue.height) 
blue_cropped_2 = blue.crop (blue_coordinates_2)

bluemix = Image.blend (blue_cropped_1, blue_cropped_2 , 0.5)

green_coordinates_1 = (100, 0, green.width-100, green.height) 
green_cropped_1 = green.crop (green_coordinates_1)

result= Image.merge ("RGB" , ( redmix , green_cropped_1 , bluemix  ))

result.thumbnail ((80, 80))
result.save ("smallfinalmonroo.jpg")






