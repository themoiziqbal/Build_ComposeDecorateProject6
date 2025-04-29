# Static methods
# These belong to class, not any specific instance. Also, they should'nt affect
# class variables or instances

class TemperatureConvertor:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return ((celsius * 9.0) / 5.0) + 32

def main():
    print(f"Freezing point of water is 0C(\
{TemperatureConvertor.celsius_to_fahrenheit(0)}F)")
    print(f"Boiling point of water is 100C(\
{TemperatureConvertor.celsius_to_fahrenheit(100)}F)")

if __name__ == '__main__':
    main()