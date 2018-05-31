class User:
	name = ""
	
	def __init__(self, name):
		self.name = name
	
	
	def sayHello(self):
		print ("Hello, my name is ", self.name)

	def sayNo():
		print("No")
		
#User objects
michael = User("Michael")
david = User("David")
eric = User("Eric")

#User object methods
michael.sayHello()
eric.sayHello()