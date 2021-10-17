def calcpostfix(expression):
	p = []
	# Conversion de notre chaine de caracteres en liste afin  de pouvoir effectuer des calculs avec des nombres 9<
	expression = expression.split()
	for i in expression:
		if i.isdigit():
			p.append(float(i))

		elif i == "+":
			a = p.pop()
			b = p.pop()
			p.append(float(b)+float(a))

		elif i == "-":
			a = p.pop()
			b = p.pop()
			p.append(float(b)-float(a))

		elif i == "/":
			a = p.pop()
			b = p.pop()
			p.append(float(b)/float(a))

		elif i == "*":
			a = p.pop()
			b = p.pop()
			p.append(float(b)*float(a))

	return p.pop()


print(calcpostfix("10 2 *"))
