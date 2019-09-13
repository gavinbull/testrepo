class MyClass:

        def __init__(self, number_in):
                self.number_in = number_in
                for number in range(1,self.number_in + 1):
                        print(number)

print_numbers = MyClass(100)
