def sum_two_smallest_nums(lst):
	lst = sorted(numero for numero in lst if numero >= 0) #recordar que Sorted es para ordenar del número más chico al más grande de una lista
	return lst[0] + lst[1]
