

class MyClass:

	def __init__(self, number_in):
		self.number_in = number_in

	def print_numbers(self): 
		for number in range(1,self.number_in + 1):
			print(number)

numbers = MyClass(100)

numbers.print_numbers()

