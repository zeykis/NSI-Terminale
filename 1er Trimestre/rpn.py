def rpn(str_):
	p = []
	for i in str_:
		if i.isdigit():
			p.append(i)
			continue
		elif i == "+":
			a = p.pop()
			b = p.pop()
			p.append(int(b)+int(a))
		elif i == "-":
			a = p.pop()
			b = p.pop()
			p.append(int(b)-int(a))
		elif i == "/":
			a = p.pop()
			b = p.pop()
			p.append(int(b)/int(a))
		elif i == "*":
			a = p.pop()
			b = p.pop()
			p.append(int(b)*int(a))
	return p.pop()


print(rpn("98-"))
