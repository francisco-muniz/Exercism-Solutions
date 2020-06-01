def convert(number):
	modulo = {
		"3": number % 3,
		"5": number % 5,
		"7": number % 7
	}

	sounds = {
		"3": "Pling",
		"5": "Plang",
		"7": "Plong"
	}

	noise = ""
	for i in ("3","5","7"):
		if modulo[i] == 0:
			noise = noise + sounds[i]

	if len(noise) > 0:
		return f'{noise}'
	else:	
		return f'{number}'