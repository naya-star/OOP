# activity1.py

# Parent Class (with Encapsulation)
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.__brand = brand  # Encapsulated attribute
        self.__model = model  # Encapsulated attribute
        self.__battery_life = battery_life  # Encapsulated attribute

    # Getter methods to access private attributes
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_battery_life(self):
        return self.__battery_life

    # Setter methods to modify private attributes
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_battery_life(self, battery_life):
        self.__battery_life = battery_life

    def turn_on(self):
        print(f"{self.get_model()} is now ON!")

    def turn_off(self):
        print(f"{self.get_model()} is now OFF!")

    def display_details(self):
        print(f"Brand: {self.get_brand()}")
        print(f"Model: {self.get_model()}")
        print(f"Battery Life: {self.get_battery_life()} hours")

    def perform_action(self):
        print(f"{self.get_model()} is performing its action!")


# Child Class with Inheritance (SmartphoneWithCamera)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        super().__init__(brand, model, battery_life)
        self.__camera_resolution = camera_resolution  # Encapsulated attribute

    # Getter method to access private attribute
    def get_camera_resolution(self):
        return self.__camera_resolution

    # Setter method to modify private attribute
    def set_camera_resolution(self, camera_resolution):
        self.__camera_resolution = camera_resolution

    def take_picture(self):
        print(f"Taking a picture with {self.get_camera_resolution()}MP camera")

    def display_details(self):
        super().display_details()
        print(f"Camera Resolution: {self.get_camera_resolution()}MP")

    # Overridden method to demonstrate polymorphism
    def perform_action(self):
        print(f"{self.get_model()} is taking a picture!")


# Example Usage
if __name__ == "__main__":
    print("=== Activity 1: Smartphone ===")

    # Smartphone instance
    phone = Smartphone("Apple", "iPhone 14", 20)
    phone.turn_on()
    phone.display_details()
    phone.perform_action()

    print("\n")

    # SmartphoneWithCamera instance
    camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S23", 18, 108)
    camera_phone.turn_on()
    camera_phone.take_picture()
    camera_phone.display_details()
    camera_phone.perform_action()  # Demonstrating polymorphism
