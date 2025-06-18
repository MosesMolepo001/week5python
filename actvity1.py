class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.battery_percent = min(100, self.battery_percent + amount)
        print(f"Battery charged to {self.battery_percent}%")

    def info(self):
        print(f"{self.brand} {self.model} - Storage: {self.storage_gb}GB, Battery: {self.battery_percent}%")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_percent=100, cooling_system=True):
        super().__init__(brand, model, storage_gb, battery_percent)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model}...")
        self.battery_percent = max(0, self.battery_percent - 10)
        print(f"Battery after gaming: {self.battery_percent}%")

    def info(self):
        super().info()
        print(f"Cooling system: {'Yes' if self.cooling_system else 'No'}")

# Example usage:
phone = Smartphone("Samsung", "Galaxy S21", 128)
phone.info()
phone.make_call("123-456-7890")
phone.charge(15)

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 5", 256)
gaming_phone.info()
gaming_phone.play_game("Call of Duty")
gaming_phone.make_call("098-765-4321")
