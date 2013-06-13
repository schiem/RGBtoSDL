def add_zeros(string):
	for i in range(8-len(string)):
		string = "0" + string
	return string



def get_values(red, green, blue):
	if red >255 or blue>255 or green>255:
		raise Exception("Number above 255")
	else:
		red, green, blue = bin(red)[2:], bin(green)[2:], bin(blue)[2:]
	return add_zeros(red), add_zeros(green), add_zeros(blue)


if __name__ == "__main__":
	red, green, blue = get_values(int(raw_input("R=")), int(raw_input("G=")), int(raw_input("B=")))
	print(int(red + green + blue, 2))




