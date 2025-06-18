# OOP Activities: Classes, Inheritance & Polymorphism

## Activity 1: Smartphone Classes with Inheritance

- `Smartphone` class represents a generic smartphone.
- Attributes: brand, model, storage size, battery percentage.
- Methods: make calls, charge battery, show info.
- `GamingSmartphone` inherits from `Smartphone`.
  - Adds a cooling system attribute.
  - Adds a method to play games (reduces battery).
  - Overrides `info()` to show cooling system status.

## Activity 2: Polymorphism Challenge 🎭

- Abstract `Vehicle` class defines a `move()` method.
- `Car`, `Plane`, and `Boat` classes inherit from `Vehicle`.
- Each subclass implements `move()` differently to represent their unique movement styles.

## How to Run

1. Save the code in a `.py` file.
2. Run it with Python 
3. Observe output for class behaviors and polymorphic method calls.

---

## Example Output

Samsung Galaxy S21 - Storage: 128GB, Battery: 100%
Calling 123-456-7890 from Samsung Galaxy S21...
Battery charged to 100%
ASUS ROG Phone 5 - Storage: 256GB, Battery: 100%
Cooling system: Yes
Playing Call of Duty on ASUS ROG Phone 5...
Battery after gaming: 90%
Calling 098-765-4321 from ASUS ROG Phone 5...
Driving 🚗
Flying ✈️
Sailing ⛵