def count_vowels(txt):
	vocales = ['a', 'e', 'i', 'o', 'u']
	C = 0
	for p in txt:
	   if p in vocales:
		    C += 1
	return C
