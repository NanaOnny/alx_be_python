FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    Celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature converted to Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    try:
        temperature_str = input("Enter temperature (e.g., 32°F or 0°C): ").strip()

        if temperature_str[-1].upper() == '°F':
            temperature = float(temperature_str[:-2])
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature} °F is {converted_temperature:.2f} °C")

        elif temperature_str[-1].upper() == '°C':
            temperature = float(temperature_str[:-2])
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature} °C is {converted_temperature:.2f} °F")

        else:
            raise ValueError("Invalid temperature format. Please enter a numeric value followed by '°F' or '°C'.")

    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value followed by '°F' or '°C'.")


if __name__ == "__main__":
    main()

