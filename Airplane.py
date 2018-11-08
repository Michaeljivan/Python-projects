class Airplane:
	def __init__(self, flightID, color, gas):
		self.flightID = flightID
		self.color = color
		self.gas = gas

	def fly(self):
		if(self.gas >= 10):
			print("Airplane "+ str(self.flightID) +" takes off!")
			self.gas -= 10

	def refillFuel(self):
		if(self.gas <= 90):
			self.gas += 10

	def getFuelLevel(self):
		return self.gas

	def getColor(self):
		return self.color

	def getFlightID(self):
		return self.flightID

 	def flightAttributes(self):
 		print('')
 		print("#### FLIGHT INFORMATION ####")
		print("Airplane Flight ID: " + str(self.getFlightID()))
		print("Airplane fuel level: " + str(self.getFuelLevel()))
		print("Airplane color: " + self.getColor())
 		print("----------------------------")
 		print('')

print("Launching flights....")
airplane1 = Airplane(001, "Blue", 89.00)
airplane2 = Airplane(002, "Red", 78.23)
airplane3 = Airplane(003, "Green", 92.30)

airplane1.flightAttributes()
airplane2.flightAttributes()
airplane3.flightAttributes()

airplane1.fly()
airplane2.fly()
airplane3.fly()


print("Airplane " + str(airplane1.getFlightID())+" fuel level is now: " + str(airplane1.getFuelLevel()))

print("Airplane " + str(airplane2.getFlightID())+" fuel level is now: " + str(airplane2.getFuelLevel()))

print("Airplane " + str(airplane3.getFlightID())+" fuel level is now: " + str(airplane3.getFuelLevel()))
