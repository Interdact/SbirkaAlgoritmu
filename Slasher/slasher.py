def slasher(arr, howMany):
	if howMany > len( arr ):
		return []
	if howMany < 0:
		return False
	if howMany == 0:
		return arr
	return arr[howMany:]

#Test
print slasher([1, 2, 3], 2)
