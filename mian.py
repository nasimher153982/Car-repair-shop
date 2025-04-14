import json
from models import Vehicle, Service
import os
from users import authenticate

DATA_FILE = 'data/records.json'

# Load data from file (if available)
def load_data():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return {"vehicles": [], "services": []}
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"vehicles": [], "services": []}

# Save data to file
def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Register a new device
def register_vehicle(data):
    name = input("owner name: ")
    contact = input("Contact number: ")
    model = input("Car model: ")
    year = input("year of production: ")
    plate = input("License plate number: ")

    vehicle = Vehicle(name, contact, model, year, plate)
    data["vehicles"].append(vehicle.__dict__)
    save_data(data)
    print("The vehicle was successfully registered.")

# New service registration
def register_service(data):
    plate = input("License plate number : ")
    service_type = input("Type of service (oil change, painting, etc.) : ")
    cost = input("Cost : ")
    duration = input("Duration (minutes) : ")

    service = Service(plate, service_type, cost, duration)
    data["services"].append(service.__dict__)
    save_data(data)
    print("The service was successfully registered.")

# Show services
def show_services(data):
    if not data["services"]:
        print("No service registered.")
        return

    print("\n--- Registered Services ---")
    print(f"{'Date':<20} | {'Plate':<10} | {'Service Type':<20} | {'Cost':<10} | {'Duration (min)':<15}")
    print("-" * 85)

    for s in data["services"]:
        print(f"{s.get('date', 'N/A'):<20} | {s.get('vehicle_plate', 'N/A'):<10} | {s.get('service_type', 'N/A'):<20} | {s.get('cost', 'N/A'):<10} | {s.get('duration', 'N/A'):<15}")


# Search
def search(data):
    query = input("Model or type of service to search for : ")
    print("\n🔍 Search results:\n")
    for s in data["services"]:
        if query.lower() in s['service_type'].lower() or query.lower() in s['vehicle_plate'].lower():
            print(f"{s['date']} - {s['vehicle_plate']} - {s['service_type']} - {s['cost']} Toman")

# Main menu
def main():
    role = authenticate()  # Get user role
    data = load_data()

    while True:
        print("\n--- Main menu ---")
        if role == 'admin':
            print("1. Register vehicle")
            print("2. Register service")
            print("3. Show services")
            print("4. Search")
            print("5. Exit")
        else:  # user role
            print("1. Show services")
            print("2. Search")
            print("3. Exit")

        choice = input("Your choice: ")

        if role == 'admin':
            if choice == '1':
                register_vehicle(data)
            elif choice == '2':
                register_service(data)
            elif choice == '3':
                show_services(data)
            elif choice == '4':
                search(data)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid selection.")
        else:  # user
            if choice == '1':
                show_services(data)
            elif choice == '2':
                search(data)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid selection.")

if __name__ == "__main__":
    main()
