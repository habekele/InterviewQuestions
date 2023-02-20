def URLify(str):
	y=""
	for x in str:
		if(x==" "):
			x="%20"
		y += x
	return(y)

good = " Im  so tired  "
print(URLify(good))