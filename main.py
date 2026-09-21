#VECHILE RENTAL SYSTEM USING PYTHON
from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, brand, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.vehicle_id}] {self.brand} {self.model} - ${self.daily_rate}/day ({status})"


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, daily_rate, seating_capacity):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.seating_capacity = seating_capacity

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.vehicle_id}] Car: {self.brand} {self.model} ({self.seating_capacity} seats) - ${self.daily_rate}/day [{status}]"


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, daily_rate, engine_cc):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.engine_cc = engine_cc

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.vehicle_id}] Bike: {self.brand} {self.model} ({self.engine_cc}cc) - ${self.daily_rate}/day [{status}]"


class RentalSystem:
    def __init__(self):
        self.inventory = {}
        self.active_rentals = {}  # Format: {vehicle_id: {"customer": name, "days": days}}

    def add_vehicle(self, vehicle):
        self.inventory[vehicle.vehicle_id] = vehicle

    def display_available_vehicles(self):
        print("\n--- Available Vehicles ---")
        available_found = False
        for vehicle in self.inventory.values():
            if vehicle.is_available:
                print(vehicle)
                available_found = True
        if not available_found:
            print("No vehicles currently available.")

    def rent_vehicle(self, vehicle_id, customer_name, days):
        if vehicle_id not in self.inventory:
            print("\nError: Invalid Vehicle ID.")
            return

        vehicle = self.inventory[vehicle_id]
        if not vehicle.is_available:
            print(f"\nError: Vehicle {vehicle_id} is already rented out.")
            return

        if days <= 0:
            print("\nError: Rental duration must be at least 1 day.")
            return

        vehicle.is_available = False
        self.active_rentals[vehicle_id] = {
            "customer": customer_name,
            "days": days
        }
        total_estimated = vehicle.daily_rate * days
        print(f"\nSuccess! Vehicle {vehicle_id} rented to {customer_name} for {days} day(s).")
        print(f"Estimated Total Bill: ${total_estimated}")

    def return_vehicle(self, vehicle_id):
        if vehicle_id not in self.inventory:
            print("\nError: Invalid Vehicle ID.")
            return

        vehicle = self.inventory[vehicle_id]
        if vehicle.is_available or vehicle_id not in self.active_rentals:
            print(f"\nError: Vehicle {vehicle_id} is not currently rented out.")
            return

        rental_info = self.active_rentals.pop(vehicle_id)
        vehicle.is_available = True
        total_bill = vehicle.daily_rate * rental_info["days"]

        print("\n" + "="*35)
        print("         RENTAL INVOICE         ")
        print("="*35)
        print(f"Customer Name : {rental_info['customer']}")
        print(f"Vehicle       : {vehicle.brand} {vehicle.model}")
        print(f"Days Rented   : {rental_info['days']}")
        print(f"Daily Rate    : ${vehicle.daily_rate}")
        print("-" * 35)
        print(f"TOTAL DUE     : ${total_bill}")
        print("="*35)


def main():
    system = RentalSystem()

    # Pre-populating inventory
    system.add_vehicle(Car("C101", "Toyota", "Camry", 50, 5))
    system.add_vehicle(Car("C102", "Honda", "Civic", 45, 5))
    system.add_vehicle(Bike("B201", "Yamaha", "R15", 25, 155))
    system.add_vehicle(Bike("B202", "Royal Enfield", "Classic 350", 35, 350))

    while True:
        print("\n=================================")
        print("  TERMINAL VEHICLE RENTAL SYSTEM ")
        print("=================================")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            system.display_available_vehicles()

        elif choice == "2":
            system.display_available_vehicles()
            v_id = input("\nEnter Vehicle ID to rent: ").strip().upper()
            name = input("Enter Customer Name: ").strip()
            try:
                days = int(input("Enter number of rental days: "))
                system.rent_vehicle(v_id, name, days)
            except ValueError:
                print("\nError: Please enter a valid number of days.")

        elif choice == "3":
            v_id = input("\nEnter Vehicle ID to return: ").strip().upper()
            system.return_vehicle(v_id)

        elif choice == "4":
            print("\nThank you for using the Vehicle Rental System. Goodbye!")
            sys.exit()

        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()