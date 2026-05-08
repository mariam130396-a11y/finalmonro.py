from PIL import Image


image = Image.open ("monro.jpg")
red, green, blue = image.split()



red = image.blend                                      
red.crop = (200, 0, image.width, image.height)  
red.crop = coordinates = (100, 0, image.width-100, image.height) 



blue=image.blend 
blue.crop = (0, 0, image.width - 200, image.height )
blue.crop = (100, 0, image.width-100, image.height) 


green.crop = (100, 0, image.width-100, image.height) 


result= Image.merge ("RGB" , ( red , green , blue  ))
result.save ("finalmonro.jpg")



result= thumbnail  ((80, 80))
result.save ("TRUMBMONRO.jpg")





