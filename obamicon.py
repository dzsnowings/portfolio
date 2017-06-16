darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

from PIL import Image
im = Image.open("obama.jpeg")
pixels = list(im.getdata())
listLength=len(pixels)

for i in range(listLength):
	rValue = pixels[i][0]
	bValue = pixels[i][1]
	gValue = pixels[i][2]
	intensity = rValue + bValue + gValue
	if intensity < 182:
		pixels[i] = darkBlue
	elif intensity >= 182 and intensity < 364:
		pixels[i] = red
	elif intensity >= 364 and intensity < 546:
		pixels[i] = lightBlue
	else:
		pixels[i]= yellow

im.putdata(pixels)
im.show()
im.save("obamicon.jpeg", "jpeg")
