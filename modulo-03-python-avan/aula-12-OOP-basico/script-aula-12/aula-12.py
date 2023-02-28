class Airplane_trip:
    """
    A class that represents an airplane trip between two airports
    """

    def __init__(self, origin: str, destination: str) -> None:
        self.origin = origin
        self.destination = destination

    def __str__(self) -> str:
        return f"Trip from {self.origin} to {self.destination}"

    def __add__(self, other_trip):
        return self + other_trip


firt_trip = Airplane_trip("Fortaleza", "Salvador")
second_trip = Airplane_trip("Salvador", "São Paulo")
third_trip = Airplane_trip("Fortaleza", "São Paulo")

print(firt_trip)
print(second_trip)
print(third_trip)
