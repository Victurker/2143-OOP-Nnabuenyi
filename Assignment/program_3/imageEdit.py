from PIL import Image, ImageFilter
import urllib,random 




def glassfilter(img, d):
    width = img.size[0]
    height = img.size[1]

    for x in range (d,width-d):
        for y in range (d,height-d):
            dnum = random.randint(0,d)
            figx = x + dnum
            figy = y + dnum
            vic =img.getpixel((figx,figy))
            img.putpixel((x,y),(vic[0],vic[1],vic[2]))

    return img
            


def flip(img):
    width = img.size[0]
    height = img.size[1]

    
    for x in range (int(width/2)):
        for y in range(height):
           orig = img.getpixel((x,y))
           opp = img.getpixel((width-1-x,y))
           img.putpixel((x,y),(opp[0],opp[1],opp[2]))
           img.putpixel((width-1-x,y),(orig[0],orig[1],orig[2]))
            

    return img    




def blur(img,blur_power=3):
    width = img.size[0]
    height = img.size[1]

    r = 0
    g = 0
    b = 0
    d = 2*blur_power * 2*blur_power
    for x in range(blur_power,width-blur_power):
        for y in range(blur_power,height-blur_power):
            for i in range(-blur_power,blur_power):
                for j in range(-blur_power,blur_power):
                    pix = img.getpixel((x+i,y+j))
                    r += pix[0]
                    g += pix[1]
                    b += pix[2]
            img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
            r = 0
            g = 0
            b = 0

    return img

def posterize(img,snap_val):
    width = img.size[0]
    height = img.size[1]
    for x in range (width):
        for y in range (height):
            orig = img.getpixel((x,y))
            r = orig[0] % snap_val
            g = orig[1] % snap_val
            b = orig[2] % snap_val

            img.putpixel((x,y),(r,g,b))

    return img



def negate(self,img=None):

        if not img == None:

            self.img = img

        for x in range(self.width):

            for y in range(self.height):

                rgb = self.img.getpixel((x,y))

                rgb2 = (255-rgb[0],255-rgb[1],255-rgb[2])


                self.img.putpixel((x,y),rgb2)

        return self.img
            


       
def warhol(img,snap):
    width = img.size[0]
    height = img.size[1]
    rec = int (255/ snap)
    
    color  =[(0, 0, 255),(255, 0, 255),(265,165,0),(255,255,0),(255,192,203)] 
    
    for x in range(width):
        for y in range(height):
            pix = img.getpixel((x,y))
            vic = int((pix[0]+pix[1] +pix[2]) /  3)
            img.putpixel ((x,y),(vic, vic, vic))
            red = vic
            war = red % snap
            if war < snap // 2:
                red -= war
            else:
                red += (snap - war)

            for i in range (1, rec + 1):

                if red < ((i * 255) /rec and red > (i - 1)) * 255/ rec:
                    img.putpixel((x,y) , (color[i % 5 -1]))
            

    return img

