class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi my name is " + self.name + " and I live in " + self.country + ".")


loc = Location("yourName", "yourCountry")
print(loc.name)
print(loc.country)

loc1 = Location("Steve", "Portugal")
loc2 = Location("Dave", "Paris")
loc3 = Location("Gwen", "Wales")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
loc.myLocation()
