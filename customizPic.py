from PIL import Image, ImageDraw, ImageFont
f = open('content.txt','r')
ttfront = ImageFont.truetype('simhei.ttf', 25) #字体大小
for i in f.readlines():
    img = Image.new('RGB', (100, 100), color = (73, 109, 137)) 
    d = ImageDraw.Draw(img)
    d.text((10,10), i.strip('\n'), fill=(255, 255, 0), font = ttfront)
    img.save(i.strip('\n')+'.png')
f.close()
