

class ThisFunction:

	def __init__(self, number_in):
		self.number_in = number_in


	def my_function(self): 

		for number in range(1,self.number_in + 1):
			print(number)

this_number = ThisFunction(8)

this_number.my_function()

