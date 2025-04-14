import datetime

# Definition of vehicle class
class Vehicle:
    def __init__(self, owner_name, contact, model, year, plate):
        self.owner_name = owner_name
        self.contact = contact
        self.model = model
        self.year = year
        self.plate = plate


# Definition of Service class
class Service:
    def __init__(self, vehicle_plate, service_type, cost, duration_minutes):
        self.vehicle_plate = vehicle_plate
        self.service_type = service_type
        self.cost = cost
        self.duration_minutes = duration_minutes
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

