from PIL import Image
im = Image.open("girl.jpg")

def avg_clr(p):
	c = list(p.getdata())
	b = len(c)
	k = list(map(sum,zip(*c)))# greatest step!
	q = (int(k[0]/b),int(k[1]/b),int(k[2]/b))# need perfected!
	return q

def divide(w,h,s):
	global im
	boxes = [(x,y,x+s,y+s) for x in range(0,w,s) for y in range(0,h,s)]
	for box in boxes:
		snip = im.crop(box)
		im.paste(avg_clr(snip),box)

def main():
	divide(im.size[0],im.size[1],20)# u can change num
	im.show()
	im.save("./marked-version.png")

main()
#