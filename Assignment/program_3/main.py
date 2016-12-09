from PIL import Image, ImageFilter
import urllib, random, imageEdit


im = Image.open("puppy.jpg")


#uncheck to see pics

#im = imageEdit.glassfilter(im,5)
#im = imageEdit.flip(im)
#im = imageEdit.blur(im,3)
#im = imageEdit.posterize(im,128)
#im = imageEdit.negate(im)
im = imageEdit.warhol(im,64)


im.show()

