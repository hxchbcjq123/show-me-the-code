from PIL import Image,ImageDraw
def addnum(image):
    title=image.resize((500,500))
    txt='4'
    title=ImageDraw.Draw(title)
    title.text((480,5),txt,fill=(255,0,0),font=None)
    del draw
    title.save('ceshi','jpeg')
if __name__==__main()__:
    image=Image.open('timg.jdp')
    addnum(image)
