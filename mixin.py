# Radio
# Wi-Fi
# Food
# Music

class WiFiMixin:
    def connect(self):
        print("You are connected to Wi-Fi.")


class MusicMixin:
    def play_music(self):
        print("Playing a music...")


class Vehicle:
    def move(self):
        pass


class Car(Vehicle, WiFiMixin):
    pass


class AirPlane(Vehicle, WiFiMixin, MusicMixin):
    pass


class MotorCycle(Vehicle):
    pass


car1 = Car()
car1.connect()

air1 = AirPlane()
air1.play_music()
