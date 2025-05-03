class Temperature:
    def __init__(self, celsius):
        self._celsius = None
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом.")
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C).")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)
print(t.fahrenheit)

t.celsius = -300