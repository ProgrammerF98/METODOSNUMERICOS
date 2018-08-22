def cumulative_sum(lst):
	return [sum(lst[:numero+1]) for numero in range(len(lst))]
